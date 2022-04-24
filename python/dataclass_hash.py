from dataclasses import dataclass
from uuid import uuid4


@dataclass
class User:
    name: str
    age: int

    def __hash__(self):
        return len(self.name) + self.age


if __name__ == "__main__":
    jang = User(name="jang", age=29)
    jong = User(name="jong", age=29)

    user_per_addr = dict()
    user_per_addr[jang] = "관악구"
    user_per_addr[jong] = "강남구"

    print(user_per_addr)
