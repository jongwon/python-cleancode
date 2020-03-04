from functools import wraps
from unittest import TestCase, main

from ch8.mrstatus import MergeRequestStatus, MergeRequestException
from ch8.framework.ut_frameworks_1 import MergeRequest as MergeRequest1
from ch8.framework.ut_frameworks_2 import MergeRequest as MergeRequest2
from ch8.framework.ut_frameworks_3 import MergeRequest as MergeRequest3, AcceptanceThreshold
import logging
import sys


class BaseCase(object):

    def setUp(self):
        self.merge_request = self.mr_cls()

    def test_1_단순_거절(self):
        self.merge_request.downvote("maintainer")
        self.assertEqual(
            self.merge_request.status.value,
            MergeRequestStatus.REJECTED.value
        )

    def test_2_이제막_생성된_건(self):
        self.assertEqual(
            self.mr_cls().status.value,
            MergeRequestStatus.PENDING.value
        )

    def test_3_검토대기(self):
        self.merge_request.upvote("core-dev")
        self.assertEqual(
            self.merge_request.status.value,
            MergeRequestStatus.PENDING.value
        )

    def test_4_승인(self):
        self.merge_request.upvote("dev1")
        self.merge_request.upvote("dev2")
        self.assertEqual(
            self.merge_request.status.value,
            MergeRequestStatus.APPROVED.value
        )

    def test_5_이중승인_검토(self):
        self.merge_request.upvote("dev1")
        self.merge_request.upvote("dev1")
        self.assertEqual(
            self.merge_request.status.value,
            MergeRequestStatus.PENDING.value
        )

    def test_6_찬성_후_반대하는_경우(self):
        self.merge_request.upvote("dev1")
        self.merge_request.upvote("dev2")
        self.merge_request.downvote("dev1")
        self.assertEqual(
            self.merge_request.status.value,
            MergeRequestStatus.REJECTED.value
        )

    def test_7_반대_후_찬성하는_경우(self):
        self.merge_request.upvote("dev1")
        self.merge_request.downvote("dev2")
        self.merge_request.upvote("dev2")
        self.assertEqual(
            self.merge_request.status.value,
            MergeRequestStatus.APPROVED.value
        )

    def test_8_invalid_type(self):
        self.assertRaises(
            TypeError, self.merge_request.upvote,
            {"invalid-object"}
        )


class ExtendedCases:
    """For the MRs that use the extended status."""

    def test_cannot_upvote_on_closed_merge_request(self):
        self.merge_request.close()
        self.assertRaises(
            MergeRequestException, self.merge_request.upvote, "dev1"
        )

    def test_cannot_downvote_on_closed_merge_request(self):
        self.merge_request.close()
        self.assertRaisesRegex(
            MergeRequestException,
            "CLOSED 상태에서는 머지 요구를 할 수 없습니다.",
            self.merge_request.downvote,
            "dev1",
        )


# class TestsUTFrameworks1(BaseCase, TestCase):
#     """tests for ut_frameworks_1"""
#     mr_cls = MergeRequest1

# class TestsUTFrameworks2(BaseCase, ExtendedCases, TestCase):
#     """tests for ut_frameworks_2"""
#     mr_cls = MergeRequest2


class TestsUTFrameworks3(BaseCase, ExtendedCases, TestCase):
    """Tests for ut_frameworks_3"""

    mr_cls = MergeRequest3

    def setUp(self):
        super().setUp()
        self.fixture_data = (
            (
                {"반대": set(), "찬성": set()},
                MergeRequestStatus.PENDING,
            ),
            (
                {"반대": set(), "찬성": {"dev1"}},
                MergeRequestStatus.PENDING,
            ),
            (
                {"반대": "dev1", "찬성": set()},
                MergeRequestStatus.REJECTED,
            ),
            (
                {"반대": set(), "찬성": {"dev1", "dev2"}},
                MergeRequestStatus.APPROVED,
            ),
            (
                {"반대": set(), "찬성": {"dev1", "dev2", "dev3"}},
                MergeRequestStatus.APPROVED,
            ),
        )

    def test_status_resolution(self):
        for context, expected in self.fixture_data:
            with self.subTest(context=context):
                status = AcceptanceThreshold(context).status()
                self.assertEqual(status.value, expected.value)


if __name__ == "__main__":
    # logging.basicConfig(stream=sys.stderr)
    # logging.getLogger("ch8.framework.test_ut_frameworks").setLevel(logging.DEBUG)
    main()