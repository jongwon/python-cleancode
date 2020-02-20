import logging
import random

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


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