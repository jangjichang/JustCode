from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_int(x: Any) -> int:
    assert type(x) in (int,)
    return x


class DataClassMixin:
    validation_method_per_field_type = {
        "str": from_str,
        "int": from_int,
    }

    @classmethod
    def from_dict(cls, d: Dict[str, Any]):
        1
        breakpoint()
        cls.__dataclass_fields__
        breakpoint()

        return super(cls, cls).__self_class__(
            name=from_str(d["name"]),
            age=from_int(d["age"]),
        )


@dataclass
class AutoNameDataClass(DataClassMixin):
    name: str
    age: int

    def __init__(self):
        pass


if __name__ == "__main__":
    # name_data_class = AutoNameDataClass(name="장지창")
    # print(name_data_class)
    a = AutoNameDataClass.from_dict({"name": "지창", "age": 5})
    print(a)
    AutoNameDataClass(name="지창", age=30)
