def minimumCost(red, blue, blueCost):
    answer = [0]
    if red[0] > blue[0] + blueCost:
        answer.append(blue[0] + blueCost)
        current_line = "BLUE"
    elif red[0] == blue[0] + blueCost:
        answer.append(blue[0] + blueCost)
        current_line = "ANY"
    else:
        answer.append(red[0])
        current_line = "RED"

    for i in range(1, len(red)):
        # breakpoint()
        if current_line == "RED":
            red_cost = red[i]
            blue_cost = blue[i] + blueCost

            if red_cost > blue_cost:
                current_line = "BLUE"
                answer.append(answer[-1] + blue_cost)
            elif red_cost == blue_cost:
                current_line = "ANY"
                answer.append(answer[-1] + blue_cost)
            else:
                answer.append(answer[-1] + red_cost)
        elif current_line == "BLUE":
            red_cost = red[i]
            blue_cost = blue[i]

            if red_cost > blue_cost:
                answer.append(answer[-1] + blue_cost)
            elif red_cost == blue_cost:
                current_line = "ANY"
                answer.append(answer[-1] + blue_cost)
            else:
                answer.append(answer[-1] + red_cost)
        elif current_line == "ANY":
            red_cost = red[i]
            blue_cost = blue[i]

            if red_cost > blue_cost:
                current_line = "BLUE"
                answer.append(answer[-1] + blue_cost)
            elif red_cost == blue_cost:
                current_line = "ANY"
                answer.append(answer[-1] + blue_cost)
            else:
                current_line = "RED"
                answer.append(answer[-1] + red_cost)

    return answer


def test_solution():
    # assert minimumCost([2,3,4], [3,1,1], 2) == [0, 2, 5, 6]
    # assert minimumCost([5], [3], 1) == [0, 4]
    # assert minimumCost([40, 20], [30, 25], 5) == [0, 35, 55]
    assert minimumCost(
        [1227, 4794, 5669, 2817, 7314, 7345, 1781], [9011, 25, 1980, 3661, 8582, 434, 1332], 3856
    ) == [
        0,
        1227,
        1227 + 3856 + 25,
        1227 + 3856 + 25 + 1980,
        1227 + 3856 + 25 + 1980 + 2817,  # 9905
        1227 + 3856 + 25 + 1980 + 2817 + 7314,  # 17219
        1227 + 3856 + 25 + 1980 + 2817 + 7314 + 434,  # 21509
        1227 + 3856 + 25 + 1980 + 2817 + 7314 + 434 + 1332,
    ]
