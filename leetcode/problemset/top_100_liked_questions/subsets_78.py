from typing import List
from itertools import combinations


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = list()

        for r in range(len(nums) + 1):
            if r == 0:
                answer.append([])
            elif r == len(nums):
                answer.append(nums)
            else:
                for combination in combinations(range(len(nums)), r):
                    subset = list()
                    for index in combination:
                        subset.append(nums[index])
                    answer.append(subset)
        return answer


def test_solution():
    is_substes([0], [[], [0]])
    is_substes([1, 2, 3], [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]])


def is_substes(problem, answer):
    solution = Solution()
    subsets = solution.subsets(problem)
    for subset in subsets[:]:
        if subset in answer:
            subsets.remove(subset)

    assert subsets == []