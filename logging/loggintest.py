"""
 로그 메시지를 포멧팅 할 수 있다.
 
"""
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(message)s"
)

def main() -> None :
    logging.debug("debug")
    logging.info("info")
    logging.warning("warning")
    logging.error("error")
    logging.critical("critical")


if __name__ == "__main__":
    main()
