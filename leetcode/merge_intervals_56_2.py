from typing import List


def solution(intervals: List[List[int]]) -> List[List[int]]:
    pass


def test_solution():
    assert solution([[1, 3]]) == [[1, 3]]
    assert solution([[1, 3], [2, 6]]) == [[1, 6]]
    assert solution([[1, 3], [2, 6], [8, 10]]) == [[1, 6], [8, 10]]
    assert solution([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
    assert solution([[1, 4], [4, 5]]) == [[1, 5]]
    assert solution([[1, 4], [0, 4]]) == [[0, 4]]
    assert solution([[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]) == [[1, 10]]
