class Solution:
    def max_power(self, s: str) -> int:
        max_power = 1
        sub_max_power = 1

        for current_character_index in range(1, len(s)):
            previous_character = s[current_character_index-1]
            current_character = s[current_character_index]

            if current_character == previous_character:
                sub_max_power += 1
            else:
                sub_max_power = 1

            if sub_max_power > max_power:
                max_power = sub_max_power

        return max_power


def test_solution():
    solution = Solution()
    assert solution.max_power(s="leetcode") == 2
    assert solution.max_power(s="abbcccddddeeeeedcba") == 5
    assert solution.max_power(s="triplepillooooow") == 5
    assert solution.max_power(s="hooraaaaaaaaaaay") == 11
    assert solution.max_power(s="tourist") == 1
    assert solution.max_power(s="cc") == 2
