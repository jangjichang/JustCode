from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        정렬이 된거라면 binary search를 알고리즘을 사용하면 되는데...
        로테이트된 거라면 어떻게 해야하나?

        절반 잘라서 양옆 비교하면 될거 같음

        left, current, right 잡고 더 작은 곳으로 이동?

        1,2,3,4,5,6,7
        7,1,2,3,4,5,6
        6,7,1,2,3,4,5
        5,6,7,1,2,3,4
        4,5,6,7,1,2,3
        3,4,5,6,7,1,2
        2,3,4,5,6,7,1


        최소를 찾고요, 그것의 앞 인덱스의 값이 자기보다 크면 그 최소를 리턴,
        아니면 계속 비교하면서 최소값 갱신
        '''
        left = 0
        right = len(nums) - 1
        min_index = 0

        '''
        바이너리 서치 구현
        left가 right보다 크거나 같으면 종료
        '''

        while left < right:
            current = (left + right) // 2

            if nums[current] < nums[current - 1] and nums[current] < nums[current + 1]:
                min_index = current
                break
            else:
                if nums[current + 1] > nums[current - 1]:
                    right = current - 1
                else:
                    left = current + 1

        while True:
            if nums[min_index] > nums[min_index - 1]:
                min_index -= 1
            else:
                break

        return nums[min_index]


def test_solution():
    sol = Solution()
    assert sol.findMin([3,4,5,1,2]) == 1
    assert sol.findMin([4,5,6,7,0,1,2]) == 0
    assert sol.findMin([11,13,15,17]) == 11
