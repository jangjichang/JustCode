import logging
from functools import wraps

logging.basicConfig(level=logging.INFO)
deco_logger = logging.getLogger("python_clean_code")


def trace_decorator(function):
    @wraps(function)
    def warpped(*args, **kwargs):
        deco_logger.info(f"{function.__qualname__} 실행")
        return function(*args, **kwargs)

    return warpped


@trace_decorator
def process_account(account_id):
    """id별 계정 처리"""
    deco_logger.info(f"{account_id} 계정 처리")
    return account_id


if __name__ == "__main__":
    process_account(1)
    help(process_account)
    print(process_account.__qualname__)
