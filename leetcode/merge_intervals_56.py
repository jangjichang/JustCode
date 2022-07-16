"""
start: datetime.datetime(2022, 4, 16, 22, 12, 26, 955234)
end:   datetime.datetime(2022, 4, 17, 0, 20, 37, 489421)
"""

from typing import List


def solution(intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort(key=lambda x: x[0])

    merged = list()

    # head의 end가 tail의 start보다 크면 머지한다. 합친다.
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:  # 비어있거나, 마지막의 end 값이 이번 interval의 시작보다 작으면 넣는다.
            merged.append(interval)
        else:  # 마지막 end 값과 인터벌 end 값 중 큰 값으로 대체한다.
            merged[-1][1] = max(merged[-1][1], interval[1])

    return merged


def test_solution():
    assert solution([[1, 3], [2, 6]]) == [[1, 6]]
    assert solution([[1, 3], [2, 6], [8, 10]]) == [[1, 6], [8, 10]]
    assert solution([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
    assert solution([[1, 4], [4, 5]]) == [[1, 5]]
    assert solution([[1, 4], [0, 4]]) == [[0, 4]]

    # Edge case
    assert solution([[1, 3], [3, 6], [4, 7]]) == [[1, 7]]
    assert solution([[1, 3]]) == [[1, 3]]
    assert solution([[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]) == [[1, 10]]  # 마지막에 모두 포함하는 경우

    # [[2, 3], [5, 6], [1, 10]] == [[1, 10]]
