from functools import wraps
from unittest import TestCase, main
import inspect

from .mrstatus import MergeRequestStatus, MergeRequestException
from .ut_frameworks_1 import MergeRequest as MergeRequest1


def print(func):

    @wraps(func)
    def exec(*args, **kwargs):
        print(func.__name__)
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

    def test_3(self):
        self.merge_request.upvote("core-dev")
        self.assertEqual(
            self.merge_request.status.value,
            MergeRequestStatus.PENDING.value
        )


class TestsUTFrameworks1(BaseCase, TestCase):
    """tests for ut_frameworks_1"""

    mr_cls = MergeRequest1


if __name__ == "__main__":
    main()