numbers = {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "quarter",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
        20: "twenty",
        30: "half",
    }


def solution(hour, minute) -> str:
    if minute == 0:
        return f"{numbers[hour]} o' clock"
    elif 1 <= minute <= 30:
        h_str = f"{numbers[hour]}"
    elif 30 < minute:
        hour += 1
        if hour == 13:
            hour = 1
        h_str = f"{numbers[hour]}"

    if minute <= 30:
        conjunction = "past"
        m_str = make_minute_string(minute)
    else:
        conjunction = "to"
        m_str = make_minute_string(60-minute)

    return " ".join([m_str, conjunction, h_str])


def test_solution():
    assert solution(5, 0) == "five o' clock"
    assert solution(5, 1) == "one minute past five"
    assert solution(5, 10) == "ten minutes past five"
    assert solution(5, 15) == "quarter past five"
    assert solution(5, 28) == "twenty eight minutes past five"
    assert solution(5, 30) == "half past five"
    assert solution(5, 40) == "twenty minutes to six"
    assert solution(5, 45) == "quarter to six"
    assert solution(5, 47) == "thirteen minutes to six"
    assert solution(11, 41) == "nineteen minutes to twelve"
    assert solution(12, 15) == "quarter past twelve"
    assert solution(12, 29) == "twenty nine minutes past twelve"
    assert solution(12, 41) == "nineteen minutes to one"


def make_minute_string(m: int) -> str:
    """
    1이면 one m
    2~30 중
        15, 30이면 quarter, half로 끝
        2~14, 16~20이면 숫자 그대로 문자로 변환하고 minutes 붙이기
        21~29면 twnety one, two등으로 문자로 변환하고 minutes 붙이기
    31~59면
        60을 뺀 분 값으로 문자열 변경.
    """
    if m == 1:
        return f"{numbers[m]} minute"
    elif m in (15, 30):
        return f"{numbers[m]}"
    elif m <= 20:
        return f"{numbers[m]} minutes"
    elif 20 < m < 30:
        units = m % 10
        tens = m - units
        return f"{numbers[tens]} {numbers[units]} minutes"


def test_make_minute_string():
    assert make_minute_string(1) == "one minute"
    assert make_minute_string(2) == "two minutes"
    assert make_minute_string(3) == "three minutes"
    assert make_minute_string(4) == "four minutes"
    assert make_minute_string(5) == "five minutes"
    assert make_minute_string(6) == "six minutes"
    assert make_minute_string(7) == "seven minutes"
    assert make_minute_string(8) == "eight minutes"
    assert make_minute_string(9) == "nine minutes"
    assert make_minute_string(10) == "ten minutes"
    assert make_minute_string(11) == "eleven minutes"
    assert make_minute_string(12) == "twelve minutes"
    assert make_minute_string(13) == "thirteen minutes"
    assert make_minute_string(14) == "fourteen minutes"
    assert make_minute_string(15) == "quarter"
    assert make_minute_string(16) == "sixteen minutes"
    assert make_minute_string(17) == "seventeen minutes"
    assert make_minute_string(18) == "eighteen minutes"
    assert make_minute_string(19) == "nineteen minutes"
    assert make_minute_string(20) == "twenty minutes"
    assert make_minute_string(21) == "twenty one minutes"
    assert make_minute_string(22) == "twenty two minutes"
    assert make_minute_string(23) == "twenty three minutes"
    assert make_minute_string(24) == "twenty four minutes"
    assert make_minute_string(25) == "twenty five minutes"
    assert make_minute_string(26) == "twenty six minutes"
    assert make_minute_string(27) == "twenty seven minutes"
    assert make_minute_string(28) == "twenty eight minutes"
    assert make_minute_string(29) == "twenty nine minutes"
    assert make_minute_string(30) == "half"


if __name__ == '__main__':
    print(solution(5, 31))
