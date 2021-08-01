import logging
from functools import wraps
import random


class ControlledException(Exception):
    """도메인에서 발생하는 일반적인 예외"""

    default_message = "controlled exception"

    def __init__(self, message=None):
        if message is None:
            message = self.default_message

        self.message = message

    def __str__(self):
        return self.message


RETRIES_LIMIT = 3


def with_retry(retries_limit=RETRIES_LIMIT, allowed_exceptions=None):
    allowed_exceptions = allowed_exceptions or (ControlledException,)

    def retry(operation):
        @wraps(operation)
        def wrapped(*args, **kwargs):
            last_raised = None
            for _ in range(retries_limit):
                try:
                    return operation(*args, **kwargs)
                except allowed_exceptions as e:
                    logging.warning(f"retrying {operation} due to {e} of {e.__class__.__qualname__}")
                    last_raised = e
            raise last_raised

        return wrapped

    return retry


@with_retry()
def run_operation():
    """실행 중 예외가 발생할 것으로 예상되는 특정 작업을 실행"""
    raise ControlledException


@with_retry(retries_limit=5)
def run_with_custom_retries_limit():
    raise ControlledException


@with_retry(allowed_exceptions=(ControlledException,))
def run_with_custom_exceptions():
    raise ControlledException


@with_retry(retries_limit=4, allowed_exceptions=(ZeroDivisionError, AttributeError))
def run_with_custom_parameters():
    num = random.randrange(0, 2)

    exception = [ZeroDivisionError, AttributeError]
    raise exception[num]


if __name__ == "__main__":
    # run_operation()
    # run_with_custom_retries_limit()
    run_with_custom_exceptions()
    # run_with_custom_parameters()
    # run_operation = retry(run_operation)
    # run_operation()
