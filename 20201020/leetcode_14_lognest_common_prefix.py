from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        return 'a'


def test_longestCommonPrefix():
    solution = Solution()

    assert solution.longestCommonPrefix(['a']) == 'aa'
