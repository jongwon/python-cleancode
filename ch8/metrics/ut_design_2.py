
import logging
import random

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class MetricsClient:

    def send(self, name, value):
        if not isinstance(name, str):
            raise TypeError("name 은 str 타입이어야 합니다.")
        if not isinstance(value, str):
            raise TypeError("value 은 str 타입이어야 합니다.")
        logger.info(" 전송 [%s=%s]", name, value);


class WrappedClient:

    def __init__(self):
        self.client = MetricsClient()

    def send(self, name, value):
        return self.client.send(str(name), str(value))

class Process:

    def __init__(self):
        self.client = WrappedClient()

    def process_iterations(self, n_iter):
        for i in range(n_iter):
            result = self.run_process()
            self.client.send("iteration.{}".format(i), result)

    def run_process(self):
        return random.randint(1, 100)


if __name__ == "__main__":
    Process().process_iterations(10)