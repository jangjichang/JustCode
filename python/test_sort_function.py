from typing import Dict


def sort_function(data: Dict):
    """
    1. 카테고리 수량 기준 내림 차순 (3 -> 2 -> 1)
    2. 카테고리 이름 내림 차순 (ㄱ -> ㄴ -> ㄷ)
    """
    return sorted(data, key=lambda x: (-x["quantity"], x["name"]))


def test_function():
    assert sort_function(
        [
            {"name": "가나", "quantity": 5},
            {"name": "다라", "quantity": 10},
            {"name": "바마", "quantity": 10},
            {"name": "마바", "quantity": 10},
            {"name": "사아", "quantity": 15},
        ]
    ) == [
        {"name": "사아", "quantity": 15},
        {"name": "다라", "quantity": 10},
        {"name": "마바", "quantity": 10},
        {"name": "바마", "quantity": 10},
        {"name": "가나", "quantity": 5},
    ]
