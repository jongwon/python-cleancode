from unittest import TestCase, main

from ch8.refactoring.refactoring_2 import (AcceptanceThreshold, MergeRequest,
                           MergeRequestException, MergeRequestExtendedStatus)


class TestMergeRequestStatus(TestCase):
    def setUp(self):
        self.merge_request = MergeRequest()

    def assert_rejected(self):
        self.assertEqual(
            self.merge_request.status, MergeRequestExtendedStatus.REJECTED
        )

    def assert_pending(self):
        self.assertEqual(
            self.merge_request.status, MergeRequestExtendedStatus.PENDING
        )

    def assert_approved(self):
        self.assertEqual(
            self.merge_request.status, MergeRequestExtendedStatus.APPROVED
        )

    def test_1_반대_1_거절(self):
        self.merge_request.downvote("maintainer")
        self.assert_rejected()

    def test_2_무반응_보류 (self):
        self.assert_pending()

    def test_3_찬성_1_보류 (self):
        self.merge_request.upvote("core-dev")
        self.assert_pending()

    def test_4_찬성_2_승인 (self):
        self.merge_request.upvote("dev1")
        self.merge_request.upvote("dev2")
        self.assert_approved()

    def test_5_중복찬성_1_보류 (self):
        self.merge_request.upvote("dev1")
        self.merge_request.upvote("dev1")
        self.assert_pending()

    def test_6_찬성_2_이후_중복_반대_1_거절 (self):
        self.merge_request.upvote("dev1")
        self.merge_request.upvote("dev2")
        self.merge_request.downvote("dev1")

        self.assert_rejected()

    def test_7_반대했던_사람이_다시_찬성_2_승인 (self):
        self.merge_request.upvote("dev1")
        self.merge_request.downvote("dev2")
        self.merge_request.upvote("dev2")

        self.assert_approved()

    def test_invalid_types(self):
        merge_request = MergeRequest()
        self.assertRaises(TypeError, merge_request.upvote, {"invalid-object"})

    def test_9_종료된_요청에_찬성한_경우_에러발생 (self):
        merge_request = MergeRequest()
        merge_request.close()
        self.assertRaises(MergeRequestException, merge_request.upvote, "dev1")
        self.assertRaisesRegex(
            MergeRequestException,
            "can't vote on a closed merge request",
            merge_request.downvote,
            "dev1",
        )


class TestAcceptanceThreshold(TestCase):
    def setUp(self):
        self.fixture_data = (
            (
                {"반대": set(), "찬성": set()},
                MergeRequestExtendedStatus.PENDING,
            ),
            (
                {"반대": set(), "찬성": {"dev1"}},
                MergeRequestExtendedStatus.PENDING,
            ),
            (
                {"반대": "dev1", "찬성": set()},
                MergeRequestExtendedStatus.REJECTED,
            ),
            (
                {"반대": set(), "찬성": {"dev1", "dev2"}},
                MergeRequestExtendedStatus.APPROVED,
            ),
        )

    def test_status_resolution(self):
        for context, expected in self.fixture_data:
            with self.subTest(context=context):
                status = AcceptanceThreshold(context).status()
                self.assertEqual(status, expected)


if __name__ == "__main__":
    main()
