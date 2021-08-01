import logging
from functools import wraps


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


class WithRetry:
    def __init__(self, retries_limit=RETRIES_LIMIT, allowed_exceptions=None):
        self.retries_limit = retries_limit
        self.allowed_exceptions = allowed_exceptions or (ControlledException,)

    def __call__(self, operation):
        @wraps(operation)
        def wrapped(*args, **kwargs):
            last_raised = None

            for _ in range(self.retries_limit):
                try:
                    return operation(*args, **kwargs)
                except self.allowed_exceptions as e:
                    logging.warning(f"retrying {operation} due to {e} of {e.__class__.__qualname__}")
                    last_raised = e
            raise last_raised

        return wrapped


@WithRetry(retries_limit=5)
def run_with_custom_retries_limit():
    raise ControlledException("데이터베이스 연결 실패")


if __name__ == "__main__":
    run_with_custom_retries_limit()
