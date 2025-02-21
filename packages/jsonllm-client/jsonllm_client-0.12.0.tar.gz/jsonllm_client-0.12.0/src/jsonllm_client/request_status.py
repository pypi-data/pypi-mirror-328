from typing import Literal, Optional

from pydantic import BaseModel, NonNegativeInt


class WorkUnitStatusCounts(BaseModel):
    total: NonNegativeInt
    cached: NonNegativeInt
    pending: NonNegativeInt
    unprocessed: NonNegativeInt
    processed: NonNegativeInt


class RequestShortStatus(BaseModel):
    request_id: str
    status: Literal["unknown", "submitted", "running", "completed", "cancelled", "timeout"]
    work_unit_status_counts: Optional[WorkUnitStatusCounts] = None

