import dataclasses
from dataclasses import dataclass
from datetime import datetime
from typing import Dict, Optional, Union


@dataclass(frozen=True)
class Group:
    group_external_key: str
    name: str
    description: str
    seller_group_count: Optional[int]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    def to_dict(self) -> Dict[str, Union[str, int]]:
        data = {}

        for field in dataclasses.fields(Group):
            value = getattr(self, field.name)
            if value is not None:
                data[field.name] = value

        return data


def test_group_to_dict():
    group = Group(
        group_external_key="123-456",
        name="파리바게트",
        description="파리바게트 매장들입니다.",
        seller_group_count=None,
        created_at=None,
        updated_at=datetime(2022, 1, 5),
    )

    for key, value in group.to_dict().items():
        assert key in ["group_external_key", "name", "description", "updated_at"]
        assert value == getattr(group, key)


def get_value(self, field_name):
    return getattr(self, field_name)
