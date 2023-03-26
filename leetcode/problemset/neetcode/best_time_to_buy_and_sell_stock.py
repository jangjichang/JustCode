from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sell = 10001
        max_profit = 0

        for p in prices:
            sell = min(p, sell)
            max_profit = max(max_profit, p - sell)

        return max_profit


def test_solution():
    solution = Solution()

    assert solution.maxProfit([7, 1, 5, 3, 6, 4]) == 5
    assert solution.maxProfit([7, 6, 4, 3, 1]) == 0
