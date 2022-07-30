from typing import List


class Solution:
    def search_range(self, nums: List[int], target: int) -> List[int]:
        index = self.find_index(nums=nums, target=target, start=0, end=len(nums)-1)
        if index == -1:
            return [-1, -1]
        else:
            return [
                self.find_start_index(nums=nums, target=target, start=index),
                self.find_end_index(nums=nums, target=target, end=index)
            ]

    def find_index(self, nums: List[int], target: int, start: int, end: int) -> int:
        if start > end:
            return -1

        mid = (start + end) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return self.find_index(nums=nums, target=target, start=start, end=mid-1)
        else:
            return self.find_index(nums=nums, target=target, start=mid+1, end=end)

    def find_start_index(self, nums: List[int], target: int, start: int) -> int:
        if nums[start] == target:
            if start-1 < 0:
                return start
            else:
                return self.find_start_index(nums=nums, target=target, start=start-1)
        else:
            return start + 1

    def find_end_index(self, nums: List[int], target: int, end: int) -> int:
        if nums[end] == target:
            if end+1 >= len(nums):
                return end
            else:
                return self.find_end_index(nums=nums, target=target, end=end+1)
        else:
            return end - 1


def test_find_index():
    solution = Solution()
    assert solution.find_index(nums=[1, 2, 3, 4, 5, 6], target=0, start=0, end=5) == -1
    assert solution.find_index(nums=[1, 2, 3, 4, 5, 6], target=1, start=0, end=5) == 0
    assert solution.find_index(nums=[1, 2, 3, 4, 5, 6], target=2, start=0, end=5) == 1
    assert solution.find_index(nums=[1, 2, 3, 4, 5, 6], target=3, start=0, end=5) == 2
    assert solution.find_index(nums=[1, 2, 3, 4, 5, 6], target=4, start=0, end=5) == 3
    assert solution.find_index(nums=[1, 2, 3, 4, 5, 6], target=5, start=0, end=5) == 4
    assert solution.find_index(nums=[1, 2, 3, 4, 5, 6], target=6, start=0, end=5) == 5
    assert solution.find_index(nums=[1, 2, 3, 4, 5, 6], target=7, start=0, end=5) == -1
    assert solution.find_index(nums=[1], target=1, start=0, end=0) == 0


def test_search_range():
    solution = Solution()
    assert solution.search_range(nums=[1, 2, 3, 4, 5, 6], target=0) == [-1, -1]
    assert solution.search_range(nums=[5, 7, 7, 8, 8, 10], target=8) == [3, 4]
    assert solution.search_range(nums=[5, 7, 7, 8, 8, 10], target=6) == [-1, -1]
    assert solution.search_range(nums=[], target=0) == [-1, -1]
    assert solution.search_range(nums=[1], target=1) == [0, 0]
    assert solution.search_range(nums=[2, 2], target=2) == [0, 1]

