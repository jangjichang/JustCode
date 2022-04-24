from dataclasses import dataclass


@dataclass
class GroupCreateRequest:
    uid: str
    name: str
    description: str


def test_dataclass_init():
    uid = "1234"
    data = {"name": "또각 치킨", "description": "또각 치킨 모음"}
    # group_create_request = GroupCreateRequest(**data, **{"uid": uid})
    # group_create_request = GroupCreateRequest(**data, **{"uid": uid})
    group_create_request = GroupCreateRequest(uid=uid, **data)

    # group_create_request = GroupCreateRequest(uid=uid, name=data['name'], description=data['description'])
    # ("name"="또각 치킨", "uid"="1234")

    assert uid == group_create_request.uid
    assert data.get("name") == group_create_request.name
    assert data.get("description") == group_create_request.description
