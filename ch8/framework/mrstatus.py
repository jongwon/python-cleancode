
from enum import Enum


class MergeRequestStatus(Enum):
    APPROVED = "approved"
    REJECTED = "rejected"
    PENDING  = "pending"


class MergeRequestExtendedStatus(Enum):
    APPROVED = "approved"
    REJECTED = "rejected"
    PENDING = "pending"
    OPEN = "open"
    CLOSED = "closed"


class MergeRequestException(Exception):
    """ merge 요청이 잘못된 경우 """