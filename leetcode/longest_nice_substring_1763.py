class Solution:
    def longest_nice_substring(self, s: str) -> str:
        longest_nice_substring = ""

        for start_index in range(len(s)):
            for end_index in range(start_index, len(s) + 1):
                substring = s[start_index:end_index]
                if self.is_nice(substring):
                    if len(substring) > len(longest_nice_substring):
                        longest_nice_substring = substring

        return longest_nice_substring

    def is_nice(self, s: str) -> bool:
        for c in s:
            if c.upper() in s and c.lower() in s:
                continue
            else:
                return False
        return True


def test_solution():
    solution = Solution()
    assert solution.longest_nice_substring(s="YazaAay") == "aAa"
    assert solution.longest_nice_substring(s="Bb") == "Bb"
    assert solution.longest_nice_substring(s="C") == ""
