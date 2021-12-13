from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        start_pointer = 0
        end_pointer = len(height) - 1
        max_area = 0

        while start_pointer < end_pointer:
            area = (end_pointer - start_pointer) * min(height[end_pointer], height[start_pointer])
            if area > max_area:
                max_area = area

            if height[end_pointer] > height[start_pointer]:
                start_pointer += 1
            else:
                end_pointer -= 1

        return max_area


def test_solution():
    solution = Solution()
    assert solution.maxArea([1, 1]) == 1
    assert solution.maxArea([4, 3, 2, 1, 4]) == 16
    assert solution.maxArea([1, 2, 1]) == 2
    assert solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49


"""
Brute Force로 작성했으나 시간 초과로 통과하지 못했다.
어떤 자료구조를 사용해야할까 생각해봤는데 딱히 적당한게 생각나지 않았다.
Brute Force로 사용하지 않고 할 수 있는 방법이 떠오르지 않았다.

키워드를 보니 그리디 알고리즘을 쓰라고 나왔다.
그리디 알고리즘은 지금의 최적해를 선택하는 것이다.

이 문제는 가장 큰 영역을 구하는 것인데, 가장 크려면 두 막대 중 작은 영역의 높이와 두 막대 사이의 거리가 커야한다.
두 막대 사이의 거리가 가장 큰 지점에서 시작하려면 양 끝에서 시작하면 된다.
양 끝에서 시작하고, 두 막대 중 높이가 작은 쪽을 한칸씩 넘기면 된다.
start_pointer의 높이가 작으면 start_pointer를 +1한다.
"""
