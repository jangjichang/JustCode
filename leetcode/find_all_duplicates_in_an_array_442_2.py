from typing import List


class Solution:
    def find_duplicates(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            while i != nums[i] - 1 and nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

        return [nums[it] for it in range(len(nums)) if it != nums[it] - 1]


def test_solution():
    solution = Solution()
    assert solution.find_duplicates([1, 1, 2]) == [1]
    assert solution.find_duplicates([1]) == []
    assert solution.find_duplicates([4, 3, 2, 7, 8, 2, 3, 1]) == [2, 3]


"""
answer  num     nums
[]       4      [4, 3, 2, -7, 8, 2, 3, 1]
[]       3      [4, 3, -2, -7, 8, 2, 3, 1]
[]       -2     [4, -3, -2, -7, 8, 2, 3, 1]
[]       -7     [4, -3, -2, -7, 8, 2, -3, 1]
[]       8     [4, -3, -2, -7, 8, 2, -3, -1]
[2]      2     [4, -3, -2, -7, 8, 2, -3, -1]
[2, 3]   -3     [4, -3, -2, -7, 8, 2, -3, -1]
[2, 3]   -1     [-4, -3, -2, -7, 8, 2, -3, -1]
"""
