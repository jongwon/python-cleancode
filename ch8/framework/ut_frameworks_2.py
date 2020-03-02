"""
 기존 예제에 OPEN, CLOSED 상태를 추가한 예제이다.
 CLOSED 상태인 경우에는 더이상 merge 를 할 수 없다.

"""
from ch8.mrstatus import MergeRequestException
from ch8.mrstatus import MergeRequestExtendedStatus as MergeRequestStatus

class MergeRequest(object):
    """  merge 요구를 추상화한 엔터티 """

    def __init__(self):
        self._context = {
            "찬성": set(),
            "반대": set()
        }
        self._status = MergeRequestStatus.OPEN

    def close(self):
        self._status = MergeRequestStatus.CLOSED

    @property
    def status(self):
        if self._status == MergeRequestStatus.CLOSED:
            return self._status

        if self._context["반대"]:
            return MergeRequestStatus.REJECTED
        elif len(self._context["찬성"]) > 2:
            return MergeRequestStatus.APPROVED
        return MergeRequestStatus.PENDING

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