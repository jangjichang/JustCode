from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # len_ = len(nums)
        # nums = set(nums)
        # ans = list()

        # for index in range(len_):
        #     if index + 1 not in nums:
        #         ans.append(index + 1)

        # return ans
        for index in range(len(nums)):
            integer = abs(nums[index])
            nums[integer - 1] = -1 * (abs(nums[integer - 1]))

        result = []
        for index, element in enumerate(nums):
            if element > 0:
                result.append(index + 1)
        return result


def test_solution():
    solution = Solution()

    assert solution.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]) == [5, 6]


if __name__ == "__main__":
    test_solution()
