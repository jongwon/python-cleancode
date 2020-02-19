"""
 status 판단을 대체할 AcceptanceThrreshold 클래스를 만든다.

"""
from .mrstatus import MergeRequestException
from .mrstatus import MergeRequestExtendedStatus as MergeRequestStatus


class AcceptanceThrreshold:

    def __init__(self, merge_req_context: dict) -> None:
        self._context = merge_req_context

    def status(self):
        if self._context["반대"]:
            return MergeRequestStatus.REJECTED
        elif len(self._context["찬성"]) >= 2:
            return MergeRequestStatus.APPROVED
        return MergeRequestStatus.PENDING


class MergeRequest(object):
    """  merge 요구를 추상화한 엔터티 """

    def __init__(self):
        self._context = {"찬성": set(), "반대": set()}
        self._status = MergeRequestStatus.OPEN

    def close(self):
        self._status = MergeRequestStatus.CLOSED

    @property
    def status(self):
        if self._status == MergeRequestStatus.CLOSED:
            return self._status
        return AcceptanceThrreshold(self._context).status()

    def _cannot_vote_if_closed(self):
        if self._status == MergeRequestStatus.CLOSED:
            raise MergeRequestException("CLOSED 상태에서는 머지 요구를 할 수 없습니다.")

    def upvote(self, by_user:str):
        self._cannot_vote_if_closed()
        self._context["반대"].discard(by_user)
        self._context["찬성"].add(by_user)

    def downvote(self, by_user:str):
        self._cannot_vote_if_closed()
        self._context["찬성"].discard(by_user)
        self._context["반대"].add(by_user)