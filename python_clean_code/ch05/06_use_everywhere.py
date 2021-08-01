import logging
from functools import wraps

logger = logging.getLogger(__name__)


class DBDriver:
    def __init__(self, dbstring):
        self.dbstring = dbstring

    def execute(self, query):
        return f"{self.dbstring}에서 쿼리 {query} 실행"


def inject_db_driver(function):
    """데이터베이스 dns 문자열을 받아서 DBDriver 인스턴스를 생성하는 데코레이터"""

    @wraps(function)
    def wrapped(dbstring):
        return function(DBDriver(dbstring))

    return wrapped


@inject_db_driver
def run_query(driver):
    return driver.execute("test_function")


if __name__ == "__main__":
    print(run_query("test_OK"))
