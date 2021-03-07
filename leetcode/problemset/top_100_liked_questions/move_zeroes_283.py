from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        last_none_zero_found_at = 0
        for index in range(len(nums)):
            if nums[index] != 0:
                nums[index], nums[last_none_zero_found_at] = nums[last_none_zero_found_at], nums[index]
                last_none_zero_found_at += 1
        
            

def test_solution():
    solution = Solution()
    problems = [
        [0, 1, 0, 3, 12],
        [1, 3, 12, 0, 0],
        [0, 1, 12, 3, 0],
        [0, 0, 1],
        [1, 0, 1],
        [0, 1, 0]
    ]

    answers = [
        [1, 3, 12, 0, 0],
        [1, 3, 12, 0, 0],
        [1, 12, 3, 0, 0],
        [1, 0, 0],
        [1, 1, 0],
        [1, 0, 0]
    ]

    for index in range(len(problems)):
        solution.moveZeroes(problems[index])
        assert problems[index] == answers[index]


if __name__ == "__main__":
    test_solution()