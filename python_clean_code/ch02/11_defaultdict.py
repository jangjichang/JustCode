from collections import defaultdict
from typing import Dict, List, Tuple


def make_defaultdict(key_value_sequnce: List[Tuple[str, int]]) -> defaultdict:
    """defaultdict을 이용해 value가 리스트인 딕셔너리를 생성합니다.

    reference: https://docs.python.org/ko/3/library/collections.html#defaultdict-examples
    """

    d = defaultdict(list)
    for color, order in key_value_sequnce:
        d[color].append(order)

    return d


def make_dict(key_value_sequnce: List[Tuple[str, int]]) -> Dict[str, List[int]]:
    d: dict = {}
    for color, order in key_value_sequnce:
        try:
            d[color].append(order)
        except KeyError:
            d[color] = [order]

    return d


if __name__ == "__main__":
    key_value_sequnce = [("yellow", 1), ("blue", 2), ("yellow", 3), ("blue", 4), ("red", 1)]
    dict_order_color = make_dict(key_value_sequnce)
    defaultdict_order_color = make_defaultdict(key_value_sequnce)

    assert dict_order_color == defaultdict_order_color
