import logging
import random

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class MetricsClient:

    def send(self, metric_name:str, metric_value:str):
        if not isinstance(metric_name, str):
            raise TypeError(" metric_name 은 str 타입이어야 합니다.")
        if not isinstance(metric_value, int): # str -> int
            raise TypeError(" metric_value 은 str 타입이어야 합니다.")
        logger.info("%s = %s 전송", metric_name, metric_value)


class Process:

    def __init__(self):
        self.client = MetricsClient()

    def process_iterations(self, n_iterations:int):
        for i in range(n_iterations):
            result = self.run_process()
            self.client.send("iteration.{}".format(i), result)

    def run_process(self):
        return random.randint(1, 100)


if __name__ == "__main__":
    Process().process_iterations(10)