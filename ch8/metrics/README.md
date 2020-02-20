
### 1.3 단위 테스트와 소프트웨어 설계

* 단위 테스트와 메인 코드는 동전의 양면과 같음
* 좋은 소프트웨어는 테스트 가능한 소프트웨어 여야 함
* **테스트 용이성**은 **클린 코드의 핵심 가치**

``` python
# 코드 테스트 : 타사에 지표를 전송하는 클라이언트


class MetricsClient:
    """
        타사에 지표를 전송하는 클라이언트 API 클래스
        name 과 value가 모두 str 타입으로 오도록 규정하고 있다.
    """

    def send(self, metric_name:str, metric_value:str):
        if not isinstance(metric_name, str):
            raise TypeError(" metric_name 은 str 타입이어야 합니다.")
        if not isinstance(metric_value, str): # str -> int
            raise TypeError(" metric_value 은 str 타입이어야 합니다.")
        logger.info("%s => %s 전송", metric_name, metric_value)


class Process:
    """
    타사 코드 : API를 호출한다.
    """
    def __init__(self):
        self.client = MetricsClient()

    def process_iterations(self, n_iterations:int):
        for i in range(n_iterations):
            result = self.run_process()
            self.client.send("api 호출 : {}".format(i), result)

    def run_process(self):
        return random.randint(1, 100)


if __name__ == "__main__":
    Process().process_iterations(10)
```
* API 는 name과 value를 모두 str 으로 주도록 요구하고 있다.
* Process 객체의 client 객체를 모의하여 테스트 할 수 있다. (Mock 테스트에서 소개)
* 메쏘드가 작은 것은 테스트 가능성면에서 매우 바람직함.

``` python
class WrappedClient:
    def __init__(self):
        self.client = MetricsClient()
    def send(self, name, value):
        return self.client.send(str(name), str(value))

class Process:
    def __init__(self):
        self.client = WrappedClient()

```
* MetricsClient 객체를 클라이언트로 직접 갖는게 아니라 WrappedClient 를 만들어 MetricsClient와 같은 interface로 구현한다.


``` python
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
if __name__ == "__main__":
    main()

```
* WrappedClient 에서 MetricsClient를 Mock 객체로 바꿔서 테스트가 가능하게 된다.
* unittest 의 main을 호출하면 파일 안에 있는 TestCase 가 실행이 된다.
* 단위 테스트는 TestCase의 test_ 로 시작하는 메쏘드들이다.
* **assert_called_with** 는 Mock 객체에서 원하는 인자로 요청이 이루어졌는지를 검사한다.
