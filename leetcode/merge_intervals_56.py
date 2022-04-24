"""
start: datetime.datetime(2022, 4, 16, 22, 12, 26, 955234)
end:   datetime.datetime(2022, 4, 17, 0, 20, 37, 489421)
"""

from typing import List


def solution(intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort(key=lambda x: x[0])

    merged = list()

    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])

    return merged


def test_solution():
    assert solution([[1, 3]]) == [[1, 3]]
    assert solution([[1, 3], [2, 6]]) == [[1, 6]]
    assert solution([[1, 3], [2, 6], [8, 10]]) == [[1, 6], [8, 10]]
    assert solution([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
    assert solution([[1, 4], [4, 5]]) == [[1, 5]]
    assert solution([[1, 4], [0, 4]]) == [[0, 4]]
    assert solution([[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]) == [[1, 10]]  # 마지막에 모두 포함하는 경우
