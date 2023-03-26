from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = set()
        nums.sort()

        for target_index in range(0, len(nums) - 1):
            left = target_index + 1
            right = len(nums) - 1

            while target_index < left < right < len(nums):
                if nums[left] + nums[right] + nums[target_index] == 0:
                    answer.add((nums[target_index], nums[left], nums[right]))
                    left += 1
                elif nums[left] + nums[right] + nums[target_index] > 0:
                    right -= 1
                else:
                    left += 1

        return [list(triplet) for triplet in answer]


if __name__ == '__main__':
    s = Solution()
    print(s.threeSum([-2, 0, 1, 1, 2]))
