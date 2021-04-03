my_numbers = (1, 1, 2, 3, 5, 8, 13, 21)
print(my_numbers[2:5])
print(my_numbers[1:7:2])

# my_numbers에 전달한 것은 실제로 슬라이스를 전달하는 것과 같다.
interval = slice(1, 7, 2)
print(my_numbers[interval])

interval = slice(None, 3)
print(my_numbers[interval])

assert my_numbers[:3] == my_numbers[interval]
