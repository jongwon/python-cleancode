
import logging

def calc():
    1/0

def main():
    try:
        calc()
    except Exception:
        logging.exception("에러...")