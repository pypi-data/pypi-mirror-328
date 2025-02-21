from typing import Union, List

from anabrid.redaccess.api.common.models.gen.log_entry import LogEntry


class JobUserCallback:
    """
    Callback class for jobs. This is just a template that can be overwritten
    by the user.

    For asynchronous job processing, this is a must.
    """

    def change_status(self, job_label: str, new_status: str):
        pass

    def log_cellback(self, log_entry: LogEntry):
        pass

    def result_callback(self, result_type: str, data: Union[str, List[float]]):
        pass

    def error_callback(self, message: str):
        pass
