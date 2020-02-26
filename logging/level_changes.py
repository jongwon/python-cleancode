import logging


def custom_log(level:int, msg:str)->None:
    logging.log(level, msg)


def main():
    """
    레벨을 인자로 줘서 찍을 수도 있다.

    """
    custom_log(logging.ERROR, "메시지")
    custom_log(logging.WARNING, "경고 메시지")


if __name__ == '__main__':
    main()