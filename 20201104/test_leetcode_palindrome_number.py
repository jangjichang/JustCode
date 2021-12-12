from collections import deque


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        digits = self.add_digit_to_list(x)

        while True:
            # O(len(x))
            if len(digits) == 0 or len(digits) == 1:
                return True

            if digits.pop() != digits.popleft():
                return False

    def add_digit_to_list(self, x):
        # O(len(x))
        digits = deque()

        while True:
            remainder = x % 10
            x = x // 10
            digits.appendleft(remainder)

            if x < 1:
                return digits


def test_isPalindrome():
    solution = Solution()
    assert solution.isPalindrome(121) == True
    assert solution.isPalindrome(-121) == False
    assert solution.isPalindrome(10) == False
    assert solution.isPalindrome(-101) == False
