from typing import List


def solution(nums: List[int]) -> int:
    """
    runs in O(n) time.
    """

    # # brute force O(n^3)
    # if not nums:
    #     return 0
    #
    # max_streak = 1
    #
    # for num in nums:
    #     current_num = num
    #     current_streak = 1
    #
    #     while current_num - 1 in nums:
    #         current_num -= 1
    #         current_streak += 1
    #
    #     max_streak = max(max_streak, current_streak)
    #
    # return max_streak

    # # sort O(n^2)
    # nums.sort()
    # current_streak = 1
    # max_streak = 1
    #
    # for index in range(1, len(nums)):
    #     if nums[index] - nums[index-1] == 1:
    #         current_streak += 1
    #     else:
    #         max_streak = max(max_streak, current_streak)
    #         current_streak = 1
    #     max_streak = max(max_streak, current_streak)
    #
    # return max_streak

    # set O(n)
    # 정렬 대신 재귀로 find. num-1 값이 없을 때만 순회 시작. 그것이 시작점이니까.
    nums_set = set(nums)
    max_streak = 1

    for num in nums_set:
        if num-1 not in nums_set:
            current_num = num
            current_streak = 1

            while current_num+1 in nums_set:
                current_streak += 1
                current_num += 1

            max_streak = max(max_streak, current_streak)

    return max_streak


def test_solution():
    assert solution([1, 2, 3, 4, 5]) == 5
    assert solution([0, 0, 0, 1, 2, 3]) == 4
    assert solution([100, 4, 200, 1, 3, 2]) == 4
