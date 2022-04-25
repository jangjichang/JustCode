from typing import List


class Solution:
    def contains_nearby_duplicate(self, nums: List[int], k: int) -> bool:
        start = 0
        sub_set = set()
        for end_index in range(len(nums)):
            if nums[end_index] in sub_set:
                return True

            sub_set.add(nums[end_index])

            if end_index - start == k:
                sub_set.remove(nums[start])
                start += 1

        return False


def test_solution():
    solution = Solution()
    assert solution.contains_nearby_duplicate(nums=[1, 2, 3, 1], k=3)
    assert solution.contains_nearby_duplicate(nums=[1, 0, 1, 1], k=1)
    assert not solution.contains_nearby_duplicate(nums=[1, 2, 3, 1, 2, 3], k=2)
