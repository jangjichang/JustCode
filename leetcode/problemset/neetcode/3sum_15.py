from typing import List


def solution(nums: List[int]) -> List[List[int]]:
    nums.sort()



def test_solution():
    assert solution(nums=[-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
    assert solution(nums=[0, 1, 1]) == []
    assert solution(nums=[0, 0, 0]) == [[0, 0, 0]]
    assert solution(nums=[0, 0, 0, 0]) == [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    assert solution(nums=[-2, 0, 1, 1, 2]) == [[-2, 0, 2], [-2, 1, 1]]
