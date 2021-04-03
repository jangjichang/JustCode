import re

EMAIL_FORMAT = re.compile(r"[^@]+@[^@]+[^@]+")


def is_valid_email(potentially_valid_email: str):
    return re.match(EMAIL_FORMAT, potentially_valid_email) is not None


class User:
    def __init__(self, username: str):
        self.username = username
        self._email = None

    # 프로퍼티는 명령-쿼리 분리 원칙 (command and query separation)을 따르기 위한 좋은 방법이다.
    # 메서드가 무언가의 상태를 변경하거나 무언가의 값을 반환하는 둘 중에 하나만 수행해야함
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, new_email):
        if not is_valid_email(new_email):
            raise ValueError(f"유효한 이메일이 아니므로 {new_email} 값을 사용할 수 없습니다.")
        self._email = new_email


if __name__ == "__main__":
    user1 = User("jsmith")
    try:
        user1.email = "jsmith@"
    except ValueError as e:
        print(e)

    user1.email = "jsmith@g.co"
    print(user1.email)
