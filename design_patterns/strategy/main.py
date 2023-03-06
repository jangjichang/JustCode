from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Context:
    """
    클라이언트의 관심사를 정의한 인터페이스.
    """
    def __init__(self, strategy: Strategy, data: List) -> None:
        """
        일반적으로 생성자로부터 전략을 결정한다. 하지만 실행 시 바꾸는 경우도 있다.
        """
        self._strategy = strategy
        self._data = data

    @property
    def strategy(self) -> Strategy:
        """
        전략 객체 하나를 갖고 있음.
        context는 전략 클래스의 구현체는 모름.
        모든 strategy이 잘 실행되어야 함
        """
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        """
        런타임에 변경 가능함
        """
        self._strategy = strategy

    def do_some_businees_logic(self) -> None:
        """
        'Context'는 알고리즘의 여러 버전을 자체적으로 구현하는 대신 일부 작업을 'Strategy' 개체에 위임합니다.
        """

        # ...
        print("Context: Sorting data using the strategy (not sure how it'll do it)")
        result = self._strategy.do_algorithm(self._data)
        print(",".join(result))
        # ...


class Strategy(ABC):
    """
    '전략' 인터페이스는 일부 알고리즘의 지원되는 모든 버전에 공통적인 작업을 선언합니다.
    '콘텍스트'는 이 인터페이스를 사용하여 콘크리트 '전략'에 의해 정의된 알고리즘을 호출한다.
    """
    @abstractmethod
    def do_algorithm(self, data: List[str]) -> List[str]:
        pass

"""
구체적인 '전략'은 기본 '전략' 인터페이스를 따르면서 알고리즘을 구현한다.
인터페이스는 '컨텍스트'에서 이들을 교환할 수 있게 해줍니다.
"""


class ConcreteStrategyA(Strategy):
    def do_algorithm(self, data: List[str]) -> List:
        return sorted(data)


class ConcreteStrategyB(Strategy):
    def do_algorithm(self, data: List[str]) -> List:
        return reversed(sorted(data))


if __name__ == '__main__':
    """
    클라이언트 코드는 구체적인 전략을 선택하여 컨텍스트에 전달합니다.
    고객은 올바른 선택을 하기 위해 전략 간의 차이를 인식해야 합니다.
    """
    context = Context(ConcreteStrategyA(), ["a", "b", "c", "z", "d", "e"])
    print("Client: Strategy is set to normal sorting.")
    context.do_some_businees_logic()
    print()

    print("Client: Strategy is set to reverse sorting.")
    context.strategy = ConcreteStrategyB()
    context.do_some_businees_logic()
