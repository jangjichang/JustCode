from typing import List, Tuple, Optional


class Solution:
    def find_length(self, nums1: List[int], nums2: List[int]) -> int:
        """
        brute force

        문자열로 조인해서 그게 같은지 본다.

        둘 중에 긴 애를 기준으로 놔두고

        짧은 애를 sub스트링을 구하면서 긴 애 안에 있는지 반복한다.
        """
        long_nums, short_nums = self.get_long_and_short_nums(nums1=nums1, nums2=nums2)
        for length in reversed(range(len(short_nums))):
            maximum_length_of_repeated_subarray = self.get_maximum_subarray_length(long_nums, short_nums[0:length])
            if maximum_length_of_repeated_subarray:
                return maximum_length_of_repeated_subarray

    def get_long_and_short_nums(self, nums1: List[int], nums2: List[int]) -> Tuple[List[int], List[int]]:
        return nums1, nums2 if len(nums1) >= len(nums2) else nums2, nums1

    def get_maximum_subarray_length(self, long_nums: List[int], short_nums: List[int]) -> Optional[int]:
        start = 0
        for


def test_solution():
    solution = Solution()
    assert solution.find_length(nums1=[1, 2, 3, 2, 1], nums2=[3, 2, 1, 4, 7]) == 3
