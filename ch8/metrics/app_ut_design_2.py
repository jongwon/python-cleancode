from unittest import TestCase, main
from unittest.mock import Mock

from ch8.metrics.ut_design_2 import WrappedClient


class WrappedClientTest(TestCase):

    def test_Mock객체로_결과_전송 (self):
        wrapped_client = WrappedClient()
        wrapped_client.client = Mock()
        wrapped_client.send("value", 1)

        wrapped_client.client.send.assert_called_with("value", "1")

"""
unittest 의 main을 호출하면 파일 안에 있는 TestCase 가 실행이 된다.
단위 테스트는 TestCase의 test_ 로 시작하는 메쏘드들이다.
assert_called_with 는 Mock 객체에서 원하는 인자로 요청이 이루어졌는지를 검사한다.
"""
if __name__ == "__main__":
    main()
