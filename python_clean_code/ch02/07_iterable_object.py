from datetime import datetime, timedelta

"""
반복 가능한 객체; list, tuple, dict, set
파이썬의 반복은 이터러블 프로토콜이라는 자체 프로토콜을 사용해 동작한다.
반복할 수 있는지 확인하기 위해 파이썬은 고수준에서 다음 두 가지를 차례로 검사한다.
1. 객체가 __next__나 __iter__ 이터레이터 메서드 중 하나를 포함하는지 여부
2. 객체가 시퀀스이고 __len__과 __getitem__를 모두 가졌는지 여부
"""


class DateRangeIterable:
    """자체 이터레이터 메서드를 가지고 있는 이터러블
    객체를 반복하려고 하면 iter() 함수를 호출한다.
    이 함수가 처음으로 하는 것은 해당 객체에 __iter__ 메서드가 있는지를 확인하는 것이다.
    만약 있으면 __iter__ 메서드를 실행한다.
    """

    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date
        self._present_day = start_date

    def __iter__(self):
        return self

    def __next__(self):
        if self._present_day >= self.end_date:
            raise StopIteration
        today = self._present_day
        self._present_day += timedelta(days=1)
        return today


for day in DateRangeIterable(datetime(2019, 1, 1), datetime(2019, 1, 5)):
    """for 루프는 앞서 만든 객체를 사용해 새로운 반복문을 시작한다.
    iter() 함수를 호출 -> 이 함수는 __iter__ 매직 메서드 호출 -> self를 반환 == 객체 자신이 이터러블임을 나타내고 있음
    따라서 각 루프의 각 단계에서마다 자신의 next() 함수를 호출한다.
    next() 함수를 호출 -> 이 함수는 __next__ 매직 메서드 호출 -> 요소를 어떻게 생산하고 하나씩 반환할 것인지 결정. 더 이상 생산 불가능하면 StopIteration 예외 발생

    """
    print(day)

r1 = DateRangeIterable(datetime(2019, 1, 1), datetime(2019, 1, 5))
r1_date = ", ".join(map(str, r1))
print(r1_date)
# 일단 한 번 실행하면 끝의 날짜에 도달한 상태이므로 이후에 호출하면 계속 StopIteration 예외가 발생한다.
# 즉, 두 개 이상의 for 루프에서 이 값을 사용하면 첫 번째 루프만 작동하고 두 번째 루프는 작동하지 않게 된다.
# print(max(r1))


class DateRangeContainerIterable:
    def __init__(self, start_date: datetime, end_date: datetime):
        self.start_date = start_date
        self.end_date = end_date

    def __iter__(self):
        current_day = self.start_date
        while current_day < self.end_date:
            yield current_day
            current_day += timedelta(days=1)


r2 = DateRangeContainerIterable(datetime(2019, 1, 1), datetime(2019, 1, 5))
r2_date = ", ".join(map(str, r2))
print("DateRangeContainerIterable")
print(r2_date)
print(max(r2))
