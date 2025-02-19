import asyncio
import requests
from typing import List, Dict, Optional, Annotated, Callable, Tuple

from anabrid.redaccess.api.common.models.gen.partition import Partition
from anabrid.redaccess.api.common.models.gen.hardware_status import HardwareStatus
from anabrid.redaccess.api.client.job_bundle import JobBundle
from anabrid.redaccess.api.client.job_user_callbacks import JobUserCallback
from anabrid.redaccess.api.common.models.gen.job_request import JobRequest
from anabrid.redaccess.api.common.models.gen.job_status import JobStatus
from anabrid.redaccess.api.common.models.gen.log import Log

from anabrid.redaccess.api.client.gen.jobs_api import JobsApi
from anabrid.redaccess.api.client.gen.system_api import SystemApi

from anabrid.redaccess.api.client.gen.configuration import Configuration
from anabrid.redaccess.api.client.gen.api_client import ApiClient


class REDACClient:
    """
    A class encapsulating REST API functions to interact with the REDAC system.
    Connects to an v0-style API and lets the user submit jobs, monitor their
    progress, listen on state changes and download results.

    This client offers both synchronous/blocking and asynchronous behavior via
    callbacks. Asynchronous functions are prefixed by "a" as is convention for
    Pythonic interfaces. Make sure you await them properly.

    All jobs are given labels, either by the user or by the client automatically.
    These labels are used in lieu to
    """

    def __init__(
        self,
        api_url: str = "https://redac.anabrid.com/api/v0",
        device_id: str = "redac1",
    ):
        self.api_url = api_url
        self.device_id = device_id

        self.runs = 0
        self.uuid_to_label = {}

        # login
        self.is_logged_in = False

    async def close(self):
        await self._api_client.close()

    ###
    # High-level, user-facing functions
    ###
    def login(self, username: str, password: str):
        self.sync_wrapper(self.alogin, username, password)

    def solve(
        self, config: dict, partition_id: int
    ) -> Tuple[str, Dict[str, List[float]]]:

        return self.sync_wrapper(self.asolve, config, partition_id)

    def log(self, job_id: str) -> str:
        log_data = self.sync_wrapper(self.get_job_logs, job_id)

        return "\n".join([t.entry for t in log_data.entries])

    def results(self, job_id: str) -> Dict[str, List[float]]:
        return self.sync_wrapper(self.get_job_results, job_id)

    def health(self) -> HardwareStatus:
        return self.sync_wrapper(self.get_system_status)

    def partitions(self) -> List[Partition]:
        num_partitions = self.sync_wrapper(self.get_num_partitions)

        return [
            self.sync_wrapper(self.get_partition, ix) for ix in range(num_partitions)
        ]

    ###
    # Job handling
    ###
    async def alogin(self, username: str, password: str):
        # retrieve API token (JWT)
        response = requests.post(
            f"{self.api_url}/auth", json={"username": username, "password": password}
        )
        if response.status_code != 200:
            raise Exception(f"Unable to authenticate ({response.status_code})")
        token = response.json().get("access_token")

        # initialize "transport layer" - auto-generated API clients
        client_config = Configuration.get_default_copy()
        client_config.host = self.api_url
        client_config.access_token = token

        self._api_client = ApiClient(configuration=client_config)
        self.client_job = JobsApi(api_client=self._api_client)
        self.client_system = SystemApi(api_client=self._api_client)

        self.is_logged_in = True

    async def asolve(self, config: dict, partition_id: int):
        try:
            # submit job
            bundle = {
                "deviceId": self.device_id,
                "partitionId": partition_id,
                "config": config,
                "opTime": 2560000,
                "icTime": 10000,
            }

            job_id = await self.submit_job(bundle)

            # wait until job complete
            status = ""
            while True:
                status = (await client.get_job_status(job_id)).status

                if status in ["COMPLETED", "FAILED"]:
                    break

            print(f"Job completed with status: {status}")

            if status == "COMPLETED":
                data = await client.get_job_results(job_id)
                return job_id, data

            return job_id, None

        except Exception as e:
            print(f"Error occurred in REDAC client: {e}")
            print("Please retry.")

    async def submit_job(self, job_config: JobBundle) -> str:
        if not self.is_logged_in:
            raise Exception("Please login first")

        job_request = JobRequest.from_dict(job_config)
        job_response = await self.client_job.submit_job(job_request)
        return job_response.job_id

    async def get_job(self, job_id: str) -> JobRequest:
        if not self.is_logged_in:
            raise Exception("Please login first")

        job_request = await self.client_job.get_job(job_id)
        return job_request

    async def get_job_status(self, job_id: str) -> JobStatus:
        if not self.is_logged_in:
            raise Exception("Please login first")

        return await self.client_job.get_job_status(job_id)

    async def get_job_logs(self, job_id: str) -> Log:
        if not self.is_logged_in:
            raise Exception("Please login first")

        return await self.client_job.get_job_logs(job_id)

    async def get_job_results(self, job_id: str) -> Dict:
        if not self.is_logged_in:
            raise Exception("Please login first")

        return await self.client_job.get_job_results(job_id)

    async def get_job_channel_data(self, job_id: str, channel: int) -> List[float]:
        if not self.is_logged_in:
            raise Exception("Please login first")

        return await self.client_job.get_job_channel_data(job_id, channel)

    async def list_job_channels(self, job_id: str):
        if not self.is_logged_in:
            raise Exception("Please login first")

        return await self.client_job.list_job_channels(job_id)

    async def delete_job(self, job_id: str):
        if not self.is_logged_in:
            raise Exception("Please login first")

        await self.client_job.delete_job(job_id)

    ###
    # Monitoring and system information
    ###
    async def get_system_status(self) -> HardwareStatus:
        if not self.is_logged_in:
            raise Exception("Please login first")

        return await self.client_system.get_device_status(self.device_id)

    async def get_num_partitions(self) -> int:
        if not self.is_logged_in:
            raise Exception("Please login first")

        return await self.client_system.get_num_partitions(self.device_id)

    async def get_partition(self, partition_id: int) -> Partition:
        if not self.is_logged_in:
            raise Exception("Please login first")

        return await self.client_system.get_partition(self.device_id, partition_id)

    async def get_devices(self):
        if not self.is_logged_in:
            raise Exception("Please login first")

        return await self.client_system.list_devices()

    ###
    # Helpers
    ###
    def sync_wrapper(self, coro, *args):
        try:
            loop = asyncio.get_running_loop()
        except RuntimeError:
            loop = None

        if loop and loop.is_running():
            return asyncio.run_coroutine_threadsafe(coro(*args), loop).result()
        else:
            return asyncio.run(coro(*args))
