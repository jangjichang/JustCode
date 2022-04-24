from typing import List


class Solution:
    def find_duplicates(self, nums: List[int]) -> List[int]:
        d = dict()
        answer = list()
        for num in nums:
            try:
                d[num]
                answer.append(num)
            except KeyError:
                d[num] = True

        return answer


def test_solution():
    solution = Solution()
    assert solution.find_duplicates([1, 1, 2]) == [1]
    assert solution.find_duplicates([1]) == []
    assert solution.find_duplicates([4, 3, 2, 7, 8, 2, 3, 1]) == [2, 3]
