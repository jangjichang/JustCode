import logging
import time
from functools import wraps

logging.basicConfig(level=logging.INFO)
deco_logger = logging.getLogger("python_clean_code")


def traced_function_wrong(function):
    @wraps(function)
    def wrapped(*args, **kwargs):
        deco_logger.info(f"{function} 함수 실행")
        start_time = time.time()
        result = function(*args, **kwargs)
        deco_logger.info("함수 {}의 실행시간 {:.2f}".format(function, time.time() - start_time))
        return result

    return wrapped


@traced_function_wrong
def process_with_delay(callback, delay=0):
    time.sleep(delay)
    return callback()
