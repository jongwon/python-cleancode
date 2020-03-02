from functools import wraps
from unittest import TestCase, main

from ch8.mrstatus import MergeRequestStatus
from ch8.framework.ut_frameworks_1 import MergeRequest as MergeRequest1
import logging
import sys


def print(func):
    log = logging.getLogger("ch8.framework.test_ut_frameworks")

    @wraps(func)
    def exec(*args, **kwargs):
        log.info(func.__name__)
        return func(*args, **kwargs)

    return exec


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


class TestsUTFrameworks1(BaseCase, TestCase):
    """tests for ut_frameworks_1"""
    mr_cls = MergeRequest1





if __name__ == "__main__":
    logging.basicConfig(stream=sys.stderr)
    logging.getLogger("ch8.framework.test_ut_frameworks").setLevel(logging.DEBUG)
    main()