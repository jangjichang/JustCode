def findMinimumEqualSum(rowA, rowB):
    sum_a = 0
    zero_count_a = 0
    sum_b = 0
    zero_count_b = 0

    for row_a in rowA:
        sum_a += row_a
        if row_a == 0:
            zero_count_a += 1

    for row_b in rowB:
        sum_b += row_b
        if row_b == 0:
            zero_count_b += 1

    if sum_a >= sum_b:
        equal_sum = sum_a + zero_count_a
        if equal_sum - sum_b - zero_count_b >= 0:
            if equal_sum < sum_a + zero_count_a * 10_000:
                return equal_sum
            else:
                return -1
        else:
            return -1
    else:
        equal_sum = sum_b + zero_count_b
        if equal_sum - sum_a - zero_count_a >= 0:
            if equal_sum < sum_b + zero_count_b * 10_000:
                return equal_sum
            else:
                return -1
        else:
            return -1


def test_findMinimumEqualSum():
    assert findMinimumEqualSum(rowA=[1, 0, 2], rowB=[1, 3, 0, 0]) == 6
    assert findMinimumEqualSum(rowA=[2, 5, 0, 1, 1], rowB=[2, 1, 0, 0]) == 10
    assert findMinimumEqualSum(rowA=[0, 0, 0], rowB=[1, 1]) == -1
    rowA = [10_000]
    for i in range(99_999):
        rowA.append(2)
    assert findMinimumEqualSum(rowA=rowA, rowB=[10000, 0]) == -1  # 209_998
    # 209_998 - 10_000 = 199_998
