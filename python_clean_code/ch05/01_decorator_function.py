import logging
from functools import wraps


class DbConnectTimeoutException(Exception):
    """도메인에서 발생하는 일반적인 예외"""

    pass


def retry(operation):
    @wraps(operation)
    def wrapped(*args, **kwargs):
        last_raised = None
        RETRIES_LIMIT = 3
        for _ in range(RETRIES_LIMIT):
            try:
                return operation(*args, **kwargs)
            except DbConnectTimeoutException as e:
                logging.warning("retrying %s", operation.__qualname__)
                last_raised = e
        raise last_raised

    return wrapped


@retry
def run_operation():
    """실행 중 예외가 발생할 것으로 예상되는 특정 작업을 실행"""
    raise DbConnectTimeoutException


if __name__ == "__main__":
    run_operation()

    # run_operation = retry(run_operation)
    # run_operation()
