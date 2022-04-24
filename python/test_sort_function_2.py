from typing import Dict


def sort_function(data: Dict):
    """
    1. 카테고리 수량 기준 내림 차순 (3 -> 2 -> 1)
    2. 카테고리 이름 내림 차순 (ㄱ -> ㄴ -> ㄷ)
    """
    sorted_data = [
        name_and_quantity[0]
        for name_and_quantity in sorted(data.items(), key=lambda item: (-item[1], item[0]))
    ]
    return sorted_data


def test_function():
    assert sort_function(
        {
            "가나": 5,
            "다라": 10,
            "바마": 10,
            "마바": 10,
            "사아": 15,
        }
    ) == ["사아", "다라", "마바", "바마", "가나"]
