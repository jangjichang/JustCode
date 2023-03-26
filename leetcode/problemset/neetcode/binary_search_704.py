def solution(nums, target):
    """
    바이너리 서치
    """
    left, right = 0, len(nums)

    while left < right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid
        else:
            left = mid + 1

    return -1


def test_solution():
    assert solution(nums = [-1,0,3,5,9,12], target = 9) == 4
    assert solution(nums = [-1,0,3,5,9,12], target = 2) == -1

