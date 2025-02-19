import os
import asyncio
import json
import typer
import datetime

from csv import writer as csv_writer
from csv import QUOTE_NONNUMERIC as QUOTE_NONNUMERIC
import matplotlib.pyplot as plt
from yaspin import yaspin
from yaspin.spinners import Spinners
from anabrid.redaccess.api.client.redac_client import REDACClient
from anabrid.redaccess.api.client.job_bundle import JobBundle

###
# Make async calls
###
from functools import wraps


def coro(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        return asyncio.run(f(*args, **kwargs))

    return wrapper


###
# Parameters and aux functions
###

API_URL = "https://redac.anabrid.com/api/v0"
DEVICE = "redac1"


async def login(client: REDACClient):
    username = os.getenv("REDAC_USERNAME", None)
    password = os.getenv("REDAC_PASSWORD", None)

    if username is None or password is None:
        raise Exception("Unable to retrieve credentials")

    await client.alogin(username, password)


###
# CLI app
###
app = typer.Typer(name="redacli")


@app.command()
@coro
async def run(
    host: str = typer.Option(API_URL, help="Host for REDAC API"),
    partition: int = typer.Option(0, help="Partition ID"),
    op_time: int = typer.Option(2, help="OP Time in seconds (max. 4)"),
    sample_rate: int = typer.Option(1000, help="Sample rate in Hz"),
    config_json: str = typer.Argument(..., help="Path to the JSON configuration file"),
):
    try:
        with open(config_json, "r") as f:
            config = json.load(f)

        job_config = {
            "deviceId": DEVICE,
            "partitionId": partition,
            "config": config,
            "opTime": op_time * 1000000000, # required as nanoseconds
            "icTime": 10000,
            "sampleRate": sample_rate,
        }

        client = REDACClient(API_URL)
        await login(client)

        with yaspin(Spinners.simpleDots, text="Submitting job...") as spinner:
            job_id = await client.submit_job(job_config)

            if job_id:
                spinner.text = f"Job submitted with ID: {job_id}"
                spinner.ok("✅")
            else:
                spinner.text = "Failed to submit job"
                spinner.fail("❌")

        with yaspin(
            Spinners.simpleDots, text="Waiting for job to complete..."
        ) as spinner:
            while True:
                status = (await client.get_job_status(job_id)).status
                if status == "COMPLETED":
                    spinner.text = f"Job {job_id} completed with status: {status}"
                    spinner.ok("✅")
                    break
                elif status == "FAILED":
                    spinner.text = f"Job {job_id} failed with status: {status}"
                    spinner.fail("❌")
                    break
                await asyncio.sleep(5)

            await client.close()
    except Exception as e:
        typer.secho(f"Error: {e}", fg=typer.colors.RED)


@app.command()
@coro
async def submit(
    host: str = typer.Option(API_URL, help="Host for REDAC API"),
    partition: int = typer.Option(0, help="Partition ID"),
    op_time: int = typer.Option(2, help="OP Time in seconds (max. 4)"),
    sample_rate: int = typer.Option(1000, help="Sample rate in Hz"),
    config_json: str = typer.Argument(..., help="Path to the JSON configuration file"),
):
    try:
        with open(config_json, "r") as f:
            config = json.load(f)

        job_config = {
            "deviceId": DEVICE,
            "partitionId": partition,
            "config": config,
            "opTime": op_time * 1000000000, # required as nanoseconds
            "icTime": 10000,
            "sampleRate": sample_rate,
        }

        client = REDACClient(API_URL)
        await login(client)

        job_id = await client.submit_job(job_config)
        print(f"Job submitted with ID: {job_id}")
        await client.close()
    except Exception as e:
        typer.secho(f"Error: {e}", fg=typer.colors.RED)


@app.command()
@coro
async def logs(
    host: str = typer.Option(API_URL, help="Host for REDAC API"),
    job_id: str = typer.Argument(..., help="Id of previously processed job"),
):
    try:
        client = REDACClient(API_URL)
        await login(client)
        log = await client.get_job_logs(job_id)
        for entry in log.entries:
            print(entry.entry)
        await client.close()
    except Exception as e:
        typer.secho(f"Error: {e}", fg=typer.colors.RED)


@app.command()
@coro
async def status(
    host: str = typer.Option(API_URL, help="Host for REDAC API"),
    job_id: str = typer.Argument(..., help="Id of previously processed job"),
):
    try:
        client = REDACClient(API_URL)
        await login(client)
        status = await client.get_job_status(job_id)
        print(f"Job {job_id} status: {status}")
        await client.close()
    except Exception as e:
        typer.secho(f"Error: {e}", fg=typer.colors.RED)


@app.command()
@coro
async def results(
    host: str = typer.Option(API_URL, help="Host for REDAC API"),
    draw: bool = typer.Option(False, help="Draw the received samples"),
    csv: str = typer.Option(None, help="Path to store CSV file holding the result data to"),
    job_id: str = typer.Argument(..., help="Id of previously processed job"),
):
    channel_data = {}

    try:
        # retrieve result data
        client = REDACClient(API_URL)
        await login(client)
        data = await client.get_job_results(job_id)

        print(json.dumps(data, indent=2))

        # retrieve job data (to generate the labels)
        path_labels = {}
        job_request = await client.get_job(job_id)

        carrier_ix = 0
        for carrier in job_request.config:
            
            for adc_ix, adc in enumerate(job_request.config[carrier].adc_channels):
                channel_str = f"/{carrier_ix}/{adc_ix}"
                path_labels[channel_str] = f"{carrier}:{adc}"

            carrier_ix += 1

        await client.close()

        if csv is not None:
            iso_ts = datetime.datetime.utcnow().isoformat() + "Z"

            with open(csv, "w") as csv_file:
                writer = csv_writer(csv_file, delimiter=";", quotechar="\"", quoting=QUOTE_NONNUMERIC)

                # metadata
                writer.writerow(["sample rate [samples/s]", job_request.sample_rate])
                writer.writerow(["op time [s]", job_request.op_time])

                writer.writerow([""])

                # actual values
                for key, values in data.items():
                    line = [iso_ts, path_labels[key]] + values
                    writer.writerow(line)


        if draw:
            # Create a new figure
            plt.figure()
            
            # Iterate over each key-value pair in the dictionary
            for key, values in data.items():
                # Plot the values with the key as the label
                plt.plot(values, label=path_labels[key])
            
            # Add labels and title
            plt.xlabel('Sample')
            plt.ylabel('Values')
            plt.title(f'Results for job {job_id}')
            
            # Add a legend to distinguish the lines
            plt.legend()
            
            # Show the plot
            plt.show()

        
    except Exception as e:
        typer.secho(f"Error: {e}", fg=typer.colors.RED)


@app.command()
@coro
async def partitions(
    host: str = typer.Option(API_URL, help="Host for REDAC API"),
):
    try:
        client = REDACClient(API_URL)
        await login(client)
        num_partitions = await client.get_num_partitions()

        for part_ix in range(num_partitions):
            partition = await client.get_partition(part_ix)
            print(f"# Partition {part_ix}")
            print(f"\t- Job queue length: {partition.queue}")
            print("\t- Carriers:")

            for c in partition.carriers:
                print(f"\t\t- {c}")

        await client.close()
    except Exception as e:
        typer.secho(f"Error: {e}", fg=typer.colors.RED)


@app.command()
@coro
async def health(
    host: str = typer.Option(API_URL, help="Host for REDAC API"),
):
    try:
        client = REDACClient(API_URL)
        await login(client)
        hw_status = await client.get_system_status()

        print(f"# Device {DEVICE}")
        print(f"\t- Mean temperature: {hw_status.temperature_mean}")
        print(f"\t- Max temperature: {hw_status.temperature_max}")
        print("\t- Temperatures:")
        for carrier_id, carrier in hw_status.carriers.items():
            for cluster_id, cluster in enumerate(carrier.clusters):
                temp_array = [
                    cluster.m0,
                    cluster.m1,
                    cluster.u,
                    cluster.c,
                    cluster.i,
                    cluster.sh,
                ]

                print(f"\t\t- /{carrier_id}/{cluster_id}: {temp_array}")

        await client.close()
    except Exception as e:
        typer.secho(f"Error: {e}", fg=typer.colors.RED)


if __name__ == "__main__":
    app()
