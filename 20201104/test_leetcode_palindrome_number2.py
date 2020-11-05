from collections import deque

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        last_half = 0

        while last_half < x:
            last_half = last_half * 10 + x % 10
            x //= 10

        return x == last_half or x == last_half // 10

def test_isPalindrome():
    solution = Solution()
    assert solution.isPalindrome(121) == True
    assert solution.isPalindrome(-121) == False
    assert solution.isPalindrome(10) == False
    assert solution.isPalindrome(-101) == False
    assert solution.isPalindrome(0) == True

