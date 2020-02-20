
from enum import Enum

class MergeRequestStatus(Enum):
    APPROVED = "approved"
    REJECTED = "rejected"
    PENDING = "pending"
    OPEN = "open"
    CLOSED = "closed"


class MergeRequestException(Exception):
    """Something went wrong with the merge request"""


class AcceptanceThreshold:
    def __init__(self, merge_request_context: dict) -> None:
        self._context = merge_request_context

    def status(self):
        if self._context["반대"]:
            return MergeRequestStatus.REJECTED
        elif len(self._context["찬성"]) >= 2:
            return MergeRequestStatus.APPROVED
        return MergeRequestStatus.PENDING


class MergeRequest:
    def __init__(self):
        self._context = {"찬성": set(), "반대": set()}
        self._status = MergeRequestStatus.OPEN

    def close(self):
        self._status = MergeRequestStatus.CLOSED

    @property
    def status(self):
        if self._status == MergeRequestStatus.CLOSED:
            return self._status
        return AcceptanceThreshold(self._context).status()

    def _cannot_vote_if_closed(self):
        if self._status == MergeRequestStatus.CLOSED:
            raise MergeRequestException("CLOSED 상태인 표결에는 merge 할 수 없습니다.")

    def upvote(self, by_user):
        self._cannot_vote_if_closed()
        self._context["반대"].discard(by_user)
        self._context["찬성"].add(by_user)

    def downvote(self, by_user):
        self._cannot_vote_if_closed()
        self._context["찬성"].discard(by_user)
        self._context["반대"].add(by_user)
