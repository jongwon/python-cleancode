import pytest

from ch8.coverage.coverage_1 import (AcceptanceThreshold, MergeRequest,
                        MergeRequestException, MergeRequestStatus)


@pytest.fixture
def rejected_mr():
    merge_request = MergeRequest()
    merge_request.downvote("dev1")
    return merge_request


def test_1_반대_1이_거절한다(rejected_mr):
    assert rejected_mr.status == MergeRequestStatus.REJECTED


def test_2_반대_1_찬성_2이면_거절한다(rejected_mr):
    rejected_mr.upvote("dev2")
    rejected_mr.upvote("dev3")
    assert rejected_mr.status == MergeRequestStatus.REJECTED


def test_3_찬성_1이면_보류한다(rejected_mr):
    rejected_mr.upvote("dev1")
    assert rejected_mr.status == MergeRequestStatus.PENDING


def test_4_찬성_2표면_승인한다(rejected_mr):
    rejected_mr.upvote("dev1")
    rejected_mr.upvote("dev2")
    assert rejected_mr.status == MergeRequestStatus.APPROVED


def test_5_표결이_없으면_보류한다 ():
    assert MergeRequest().status == MergeRequestStatus.PENDING


def test_6_찬성_1이면_보류한다():
    merge_request = MergeRequest()
    merge_request.upvote("core-dev")
    assert merge_request.status == MergeRequestStatus.PENDING


def test_7_찬성2_승인 ():
    merge_request = MergeRequest()
    merge_request.upvote("dev1")
    merge_request.upvote("dev2")

    assert merge_request.status == MergeRequestStatus.APPROVED


def test_8_찬성1_중복투표_보류 ():
    merge_request = MergeRequest()
    merge_request.upvote("dev1")
    merge_request.upvote("dev1")

    assert merge_request.status == MergeRequestStatus.PENDING


def test_9_찬성을_반대로_수정한경우_거절 ():
    merge_request = MergeRequest()
    merge_request.upvote("dev1")
    merge_request.upvote("dev2")
    merge_request.downvote("dev1")

    assert merge_request.status == MergeRequestStatus.REJECTED


def test_10_downvote_to_upvote():
    merge_request = MergeRequest()
    merge_request.upvote("dev1")
    merge_request.downvote("dev2")
    merge_request.upvote("dev2")

    assert merge_request.status == MergeRequestStatus.APPROVED


def test_11_invalid_types():
    merge_request = MergeRequest()
    pytest.raises(TypeError, merge_request.upvote, {"invalid-object"})


def test_12_cannot_vote_on_closed_merge_request():
    merge_request = MergeRequest()
    merge_request.close()
    pytest.raises(MergeRequestException, merge_request.upvote, "dev1")
    with pytest.raises(
        MergeRequestException, match="CLOSED 상태인 표결에는 merge 할 수 없습니다."
    ):
        merge_request.downvote("dev1")


@pytest.mark.parametrize(
    "context,expected_status",
    (
        ({"반대": set(), "찬성": set()}, MergeRequestStatus.PENDING),
        (
            {"반대": set(), "찬성": {"dev1"}},
            MergeRequestStatus.PENDING,
        ),
        ({"반대": "dev1", "찬성": set()}, MergeRequestStatus.REJECTED),
        (
            {"반대": set(), "찬성": {"dev1", "dev2"}},
            MergeRequestStatus.APPROVED,
        ),
    ),
)
def test_acceptance_threshold_status_resolution(context, expected_status):
    assert AcceptanceThreshold(context).status() == expected_status
