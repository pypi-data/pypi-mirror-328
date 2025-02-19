from pydantic import BaseModel, Field
from anabrid.redaccess.api.common.models.gen.job_request import JobRequest


class JobBundle(BaseModel):
    partition_id: int = Field(
        ..., description="(Logical partition id in which to submit the job)"
    )
    label: str = Field(
        None,
        description="Label that may be used to identify the job. If none is provided one will be set by the runtime.",
    )
    config: JobRequest = Field(
        ...,
        description="The actual parition configuration describing the circuit and its run parameters.",
    )
