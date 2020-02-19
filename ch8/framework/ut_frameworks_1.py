
from .mrstatus import MergeRequestStatus

class MergeRequest(object):
    """  merge 요구를 추상화한 엔터티 """

    def __init__(self):
        self._context = {"찬성": set(), "반대": set()}

    @property
    def status(self):
        if self._context["반대"]:
            return MergeRequestStatus.REJECTED
        elif len(self._context["찬성"]) > 2:
            return MergeRequestStatus.APPROVED
        return MergeRequestStatus.PENDING

    def upvote(self, by_user:str):
        self._context["반대"].discard(by_user)
        self._context["찬성"].add(by_user)

    def downvote(self, by_user:str):
        self._context["찬성"].discard(by_user)
        self._context["반대"].add(by_user)