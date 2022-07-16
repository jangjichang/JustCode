from collections import defaultdict


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        max_window_size = 0

        for i in range(len(s)):
            sub_string = s[i:]
            max_window_size = max(max_window_size, self.get_max_window_size(s=sub_string, k=k))
        return max_window_size

    def get_max_window_size(self, s: str, k: int) -> int:
        max_window_size = 0
        frequency_per_character_window = defaultdict(int)
        for i in s:
            frequency_per_character_window[i] += 1

            is_qualified_max_window = True
            for frequency in frequency_per_character_window.values():
                if frequency < k:
                    is_qualified_max_window = False

            if is_qualified_max_window:
                max_window_size = max(max_window_size, sum(frequency_per_character_window.values()))

        for i in s[:-1]:
            frequency_per_character_window[i] -= 1

            is_qualified_max_window = True
            for frequency in frequency_per_character_window.values():
                if frequency < k:
                    is_qualified_max_window = False

            if is_qualified_max_window:
                max_window_size = max(max_window_size, sum(frequency_per_character_window.values()))

        return max_window_size


def test_solution():
    solution = Solution()
    assert solution.longestSubstring(s="aaabb", k=3) == 3
    assert solution.longestSubstring(s="ababbc", k=2) == 5
    assert solution.longestSubstring(s="bbaaacbd", k=3) == 3
