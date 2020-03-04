
from unittest.mock import MagicMock
from unittest import mock
from ch8.constants import STATUS_ENDPOINT
from ch8.mock.mock_2 import BuildStatus


@mock.patch("ch8.mock.mock_2.requests")
def test_build_notification_sent(mock_requests):
    build_date = "2018-01-01T00:00:01"
    with mock.patch("ch8.mock.mock_2.BuildStatus.build_date", return_value=build_date):
        BuildStatus.notify(123, "OK")

    expected_payload = {"id": 123, "status": "OK", "built_at": build_date}
    mock_requests.post.assert_called_with(
        STATUS_ENDPOINT, json=expected_payload
    )
