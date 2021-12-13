class Solution:
    def max_power(self, s: str) -> int:
        previous_character = s[0]
        max_power = 1
        sub_max_power = 1

        for current_character in s[1:]:
            if current_character == previous_character:
                sub_max_power += 1
                if sub_max_power > max_power:
                    max_power = sub_max_power
            else:
                if sub_max_power > max_power:
                    max_power = sub_max_power
                sub_max_power = 1
            previous_character = current_character

        return max_power


def test_solution():
    solution = Solution()
    assert solution.max_power(s="leetcode") == 2
    assert solution.max_power(s="abbcccddddeeeeedcba") == 5
    assert solution.max_power(s="triplepillooooow") == 5
    assert solution.max_power(s="hooraaaaaaaaaaay") == 11
    assert solution.max_power(s="tourist") == 1
    assert solution.max_power(s="cc") == 2
