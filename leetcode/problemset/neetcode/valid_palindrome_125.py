def solution(s: str) -> bool:
    # # unicode를 활용한 풀이
    # lower_s = ""
    #
    # for c in s:
    #     if ord('A') <= ord(c) <= ord('Z') or ord('0') <= ord(c) <= ord('9') or ord('a') <= ord(c) <= ord('z'):
    #         lower_s += c.lower()
    #
    # index = int(len(lower_s) / 2)
    # length = len(lower_s)
    # for i in range(index):
    #     if lower_s[i] != lower_s[length-1-i]:
    #         return False
    #
    # return True

    # two pointer
    left_index = 0
    right_index = len(s) - 1

    while left_index < right_index:
        while not s[left_index].isalnum() and left_index < right_index:
            left_index += 1

        while not s[right_index].isalnum() and left_index < right_index:
            right_index -= 1

        if s[left_index].lower() != s[right_index].lower():
            return False

        left_index += 1
        right_index -= 1

    return True


def test_solution():
    assert solution(s="A man, a plan, a canal: Panama")
    assert solution(s="0P") is False
    assert solution(s="a_ba")
    assert solution(s=".,")
    assert solution(s="race a car") is False
