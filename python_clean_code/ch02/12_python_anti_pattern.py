from collections import UserList
from typing import Union

# 변경 가능한(mutable) 파라미터의 기본 값

# anti-pattern
# def wrong_user_display(user_metadata: dict = {"name": "John", "age": 30}):
#     """기본 값을 사용해 함수를 호출하면 기본 데이터로 사용될 dict를 한 번만 생성하고 user_metadata는 이것을 가리킨다."""
#     name = user_metadata.pop("name")
#     age = user_metadata.pop("age")
#     return f"{name} {age}"


def wrong_user_display(user_metadata: Union[dict, None] = None):
    """함수는 자체 스코프와 생명주기를 가지므로 None이 나타날 때마다 user_metadata를 사전에 할당한다."""
    if user_metadata is None:
        user_metadata = {"name": "John", "age": 30}
    name = user_metadata.pop("name")
    age = user_metadata.pop("age")
    return f"{name} {age}"


print(wrong_user_display())
print(wrong_user_display({"name": "Jane", "age": 25}))
print(wrong_user_display())


# bulit-in 타입 확장
# list, str, dict와 같은 내장 타입을 확장하는 올바른 방법은 collections 모듈을 사용하는 것이다.

# class BadList(list):
#     def __getitem__(self, index):
#         value = super().__getitem__(index)
#         if index % 2 == 0:
#             prefix = "짝수"
#         else:
#             prefix = "홀수"
#         return f"[{prefix} {value}]"


# b1 = BadList((0, 1, 2, 3, 4, 5))
# print(b1[0])
# print(b1[1])
# print("".join(b1))


class GoodList(UserList):
    def __getitem__(self, index):
        value = super().__getitem__(index)
        if index % 2 == 0:
            prefix = "짝수"
        else:
            prefix = "홀수"
        return f"[{prefix} {value}]"


g1 = GoodList((0, 1, 2, 3, 4, 5))
print(g1[0])
print(g1[1])
print("".join(g1))
