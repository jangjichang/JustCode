class Solution:
    def min_add_to_make_valid(self, s: str) -> int:
        min_parentheses = ""
        for c in s:
            if len(min_parentheses) == 0:
                min_parentheses = f"{min_parentheses}{c}"
            else:
                if min_parentheses[-1] == "(" and c == ")":
                    min_parentheses = min_parentheses[:-1]
                else:
                    min_parentheses = f"{min_parentheses}{c}"

        return len(min_parentheses)


def test_solution():
    solution = Solution()
    assert solution.min_add_to_make_valid(s="())") == 1
    assert solution.min_add_to_make_valid(s="(((") == 3
    assert solution.min_add_to_make_valid(s="()))((") == 4
