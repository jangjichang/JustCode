# 방어적(defensive) 프로그래밍

방어적 프로그래밍은 DbC와는 다소 다른 접근 방식을 따른다. 계약에서 예외를 발생시키고 실패하게 되는 모든 조건을 기술하는 대신 객체, 함수 또는 메서드와 같은 코드의 모든 부분을 유효하지 않은 것으로부터 스스로 보호할 수 있게 하는 것이다.

방어적 프로그래밍의 주요 주제는 예상할 수 있는 시나리오의 오류를 처리하는 방법과 (불가피한 조건에 의해서) 발생하지 않아야 하는 오류를 처리하는 방법에 대한 것이다. 전자는 에러 핸들링 프로시저에 대한 것이며, 후자는 assertion에 대한 것이다. 이 두 가지 주제는 다음 섹션에서 확인할 것이다.

## 에러 핸들링

오류가 발생하기 쉬운 상황에서 에러 핸들링 프로시저를 사용하는데 일반적으로 데이터 입력 확인 시 자주 사용된다.

에러 핸들링의 주요 목적은 예상되는 에러에 대해서 실행을 계속할 수 있을지 아니면 극복할 수 없는 오류여서 프로그램을 중단할지를 결정하는 것이다. 프로그램에서 에러를 처리하는 방법에는 여러 가지가 있지만 모든 것을 처리할 수 있는 것은 아니다. 에러 처리 방법의 일부는 다음과 같다.
- 값 대체(substitution)
- 에러 로깅
- 예외 처리

## 값 대체

값 대체; 일부 시나리오에서는 오류가 있어 소프트웨어가 잘못된 값을 생성하거나 전체가 종료될 위험이 있을 경우 결과 값을 안전한 다른 값으로 대체할 수 있다.

대체 값이 실제로 안전한 옵션인 경우에 한해 신중하게 선택해야 한다. 이 결정을 내리는 것은 견고성과 정확성 간의 트레이드오프이다. 소프트웨어 프로그램은 예상치 못한 상황에서도 실패하지 않아야 견고하다고 할 수 있다. 그러나 무조건 실패하지 않는 것이 항상 옳은 것은 아니다.

약간 다른 방향으로 보다 안전한 방법을 택하자면 제공되지 않은 데이터에 기본 값을 사용하는 것이다. 설정되지 않은 환경 변수의 기본 값, 설정 파일의 누락된 항목 또는 함수의 파라미터와 같은 것들은 기본 값으로 동작이 가능한 것들이다. 예를 들어 dict에는 get메서드의 두번째 파라미터를 사용하면 기본 값을 나타낼 수 있다.

```
>> configuration = {"dbport": 5432}
>> configuration.get("dbhost", "localhost)
'localhost'
>> configuration.get("dbport")
5432
```

환경 변수에도 유사한 API가 있다.
```
>> import os
>> os.getenv("DBHOST")
'localhost'
>> os.getenv("DBPORT, 5432)
5432
```

## 예외 처리

잘못되거나 누락된 입력 데이터가 있는 경우처럼 사전조건 검증에 실패한 경우가 있다. 함수 호출 실패는 함수 자체의 문제가 아니라 외부 컴포넌트 중 하나의 문제로 인한 것일 수도 있다. 이런 경우 적절하게 인터페이스를 설계하면 쉽게 디버깅할 수 있다. 함수는 심각한 오류에 대해 명확하고 분명하게 알려줘서 적절하게 해결할 수 있도록 해야 한다.

이것이 바로 예외 메커니즘이다. 예외적인 상황을 명확하게 알려주고 원래의 비즈니스 로직에 따라 흐름을 유지하는 것이 중요하다.

예외를 사용하여 시나리오나 비즈니스 로직을 처리하려고 하면 프로그램의 흐름을 읽기 어려워진다. 호출자가 알아야만 하는 실질적인 문제가 있을 경우에는 예외를 발생시켜야 한다. 프로그램이 꼭 처리해야 하는 정말 예외적인 비즈니스 로직을 except 블록과 혼합하여 사용하면 상황이 악화된다. 이렇게 되면 유지보수가 필요한 핵심 논리와 오류를 구별하는 것이 어려워진다.

마지막으로 중요한 개념이 하나 더 있다. 예외는 대개 호출자에게 잘못을 알려주는 것이다. 예외는 캡슐화를 약화시키기 때문에 신중하게 사용해야 한다. 함수에 예외가 많을수록 호출자가 호출하는 함수에 대해 더 많은 것을 알아야만 한다. 그리고 함수가 너무 많은 예외를 발생시키면 문맥에서 자유롭지 않다는 것을 의미한다. 왜냐하면 호출할 때마다 발생 가능한 부작용을 염두에 두고 문맥을 유지해야하기 때문이다.

이것은 함수가 응집력이 약하고 너무 많은 책임을 가지고 있다는 것을 알기 위한 경험적 확인 방법이 될 수도 있다. 예외가 너무 많이 발생하면 여러 개의 작은 것으로 나눠야한다는 신호일 수 있다.

다음은 파이썬의 예외와 관련된 몇 가지 권장 사항이다.

### *올바른 수준의 추상화 단계에서 예외 처리*

예외는 오직 한 가지 일을 하는 함수의 한 부분이어야 한다. 함수가 처리하는 (또는 발생시키는) 예외는 캡슐화된 로직과 일치해야 한다.

다음은 서로 다른 수준의 추상화를 혼합하는 예제이다. 애플리케이션에서 디코딩한 데이터를 외부 컴포넌트에 전달하는 객체를 상상해보자.

코드는 `02_exception_in_abstract_bad_case.py` 참고

deliver_event 함수에서 ValueError와 ConnectionError는 무슨 관계일까? 별로 관계가 없다. 이렇게 매우 다른 유형의 오류를 살펴봄으로써 책임을 어떻게 분산해야 하는지에 대한 아이디어를 얻을 수 있다.

ValueError는 