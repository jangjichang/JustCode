import sys
from typing import List


class Solution:
    def find_max_average(self, nums: List[int], k: int) -> float:
        max_sum = -sys.float_info.max
        window_sum = 0
        start = 0

        for end_index in range(len(nums)):
            window_sum += nums[end_index]

            if end_index - start + 1 == k:
                max_sum = max(max_sum, window_sum)
                window_sum -= nums[start]
                start += 1

        return max_sum / k


def test_smoke():
    solution = Solution()
    assert solution.find_max_average(nums=[1, 12, -5, -6, 50, 3], k=4) == 12.75
    assert solution.find_max_average(nums=[5], k=1) == 5.0
    assert solution.find_max_average(nums=[-1], k=1) == -1
