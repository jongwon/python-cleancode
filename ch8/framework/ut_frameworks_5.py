"""
  클래스에 직접 테스트 코드를 만들어 넣는다.

"""
import pytest

from .mrstatus import MergeRequestException
from .mrstatus import MergeRequestExtendedStatus as MergeRequestStatus


class AcceptanceThrreshold:
    """ 수용여부를 판단하는 객체
        1. 반대가 있으면 거절
        2. 찬성이 1명 뿐이면 보류
        3. 찬성이 2명 이상이면 승인
    """
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


@pytest.fixture
def rejected_mr():
    mr = MergeRequest()
    mr.downvote("dev1")
    mr.upvote("dev2")
    mr.upvote("dev3")
    mr.downvote("dev4")
    return mr

def test_1_단순_거절(rejected_mr:MergeRequest):
    assert rejected_mr.status == MergeRequestStatus.REJECTED

def test_2_찬성이_있어도_거절되는경우(rejected_mr:MergeRequest):
    rejected_mr.upvote("dev2")
    rejected_mr.upvote("dev3")
    assert rejected_mr.status == MergeRequestStatus.REJECTED

def test_3_찬성이_1표라_보류됨(mr:MergeRequest):
    mr.upvote("dev")
    assert mr.status == MergeRequestStatus.PENDING

def test_4_찬성_2표라_승인됨(mr:MergeRequest):
    mr.upvote("dev1")
    mr.upvote("dev2")
    assert mr.status == MergeRequestStatus.APPROVED

def test_5(mr:MergeRequest):
    pass

def test_6(mr:MergeRequest):
    pass

def test_7(mr:MergeRequest):
    pass

def test_8(mr:MergeRequest):
    pass

def test_9(mr:MergeRequest):
    pass

def test_10(mr:MergeRequest):
    pass

def test_11(mr:MergeRequest):
    pass

def test_12(mr:MergeRequest):
    pass

@pytest.mark.parametrize(
    "context,expected_status",
    (
            ({
                "반대": set(),
                "찬성": set()
             }, MergeRequestStatus.PENDING),
            ({
                "반대": set(),
                "찬성": {"dev1"}
             }, MergeRequestStatus.PENDING),
            ({
                "반대": set(),
                "찬성": {"dev1", "dev2"}
             }, MergeRequestStatus.APPROVED),
    ),
)
def test_acceptance_threshold_status_resolution(context, expected_status):
    assert AcceptanceThrreshold(context).status() == expected_status
