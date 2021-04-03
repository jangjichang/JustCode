import contextlib
from subprocess import run


def stop_database():
    run("systemctl stop postgresql.service", check=True)


def start_database():
    run("systemctl start postgresql.service", check=True)


class DBHandler:
    """데이터베이스 작업 관련 컨텍스트 매니저입니다.

    문제점;
    1. __enter__의 반환 값은 쓸모가 없다. __enter__에서 무언가를 반환하는 것이 좋은 습관이다.
    2. 유지보수 작업과 상관없이 백업을 실행한다. 또한 백업에 오류가 있어도 여전히 __exit__를 호출한다.
    3. __exit__에서 특별한 작업을 할 필요가 없다면 아무것도 반환하지 않아도 된다. True를 반환하면 잠재적으로 발생한 예외를 호출자에게 전파하지 않고 멈춘다는 것을 뜻한다.
    """

    def __enter__(self):
        stop_database()
        return self

    def __exit__(self, exc_type, ex_value, ex_traceback):
        start_database()


def db_backup():
    run("pg_dump database", check=True)


def main():
    with DBHandler():
        db_backup()


@contextlib.contextmanager
def db_handler():
    """yield문을 사용했으므로 제너레이터 함수가 된다.
    데코레이터를 적용하면 yield 문 앞의 모든 것은 __enter__ 메서드의 일부처럼 취급된다.
    여기서 생성된 값은 컨텍스트 관리자의 평가 결과로 사용된다.
    __enter__의 반환 값과 같은 역할을 하는 것으로 as x: 와 같은 형태로 변수에 할당할 수 있다.
    이 함수에서는 반환되는 것이 없다.

    yield 문 다음에 오는 모든 것들을 __exit__ 로직으로 볼 수 있다.

    컨텍스트 매니저를 작성하면 기존 함수를 리팩토링하기 쉬운 장점이 있다.
    어느 특정 객체에도 속하지 않은 컨텍스트 관리자가 필요한 경우 좋은 방법이다.
    매직 메서드를 추가하면 업무 도메인에 보다 얽히게 되며, 책임이 커지고, 어쩌면 하지 않아도 될 것들을 지원해야만 한다.

    회사에서 적용해보기)
    특정 컬렉션 관련된 작업을 할 때 인덱스를 생성하는데, 이를 자동으로 할 수 있도록 컨텍스트 매니저를 만드는 것은 어떨까?
    """
    stop_database()
    yield
    start_database()


with db_handler():
    db_backup()


class dbhandler_decorator(contextlib.ContextDecorator):
    """데코레이터이므로 with문 없이 사용 가능
    완전히 독립적으로 사용 가능
    재사용성이 가능하다.
    단점; 컨텍스트 관리자 내부에서 사용하고자 하는 객체를 얻을 수 없다.
    예를들어, __enter__로 반환되는 값을 받을 수 없다. 이렇게 하려면 `with offline_backup() as bp`로 사용해야한다.
    """

    def __enter__(self):
        stop_database()

    def __exit__(self, ext_type, ex_value, ex_traceback):
        start_database()


@dbhandler_decorator()
def offline_backup():
    run("pg_dump database", check=True)
