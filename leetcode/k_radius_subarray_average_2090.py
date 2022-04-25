from typing import List


class Solution:
    def get_averages(self, nums: List[int], k: int) -> List[int]:
        k_radius_subarray_averages = []
        start = 0

        for end_index in range(len(nums)):
            if end_index - k >= 0 and end_index + k < len(nums):
                if start == 0:
                    sub_array_sum = sum(nums[: k * 2 + 1])
                    k_radius_subarray_averages.append(sub_array_sum // (k * 2 + 1))
                    start += 1
                else:
                    sub_array_sum -= nums[start - 1]
                    sub_array_sum += nums[end_index + k]
                    k_radius_subarray_averages.append(sub_array_sum // (k * 2 + 1))
                    start += 1
            else:
                k_radius_subarray_averages.append(-1)

        return k_radius_subarray_averages


def test_solution():
    solution = Solution()
    assert solution.get_averages(nums=[7, 4, 3, 9, 1, 8, 5, 2, 6], k=3) == [-1, -1, -1, 5, 4, 4, -1, -1, -1]
    assert solution.get_averages(nums=[100000], k=0) == [100000]
    assert solution.get_averages(nums=[8], k=100000) == [-1]
