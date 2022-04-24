class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        return max(list(map(self.get_sub_string_length, [s[i:] for i in range(len(s))])))

    def get_sub_string_length(self, s: str) -> int:
        sub_string = set()
        for c in s:
            if c not in sub_string:
                sub_string.add(c)
            else:
                return len(sub_string)
        return len(sub_string)


def test_solution():
    solution = Solution()
    assert solution.lengthOfLongestSubstring("abcabcbb") == 3
    assert solution.lengthOfLongestSubstring("bbbbb") == 1
    assert solution.lengthOfLongestSubstring("pwwkew") == 3
    assert solution.lengthOfLongestSubstring("dvdf") == 3
    assert solution.lengthOfLongestSubstring("") == 0
