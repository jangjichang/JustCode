# 좋은 코드의 일반적인 특징

좋은 소프트웨어는 좋은 디자인으로부터 나온다. 클린 코드에 대해서 말하면 디자인보다는 세부 구현의 모범 사례에 대해서만 생각하기 쉽다. 하지만 이는 잘못된 생각이다. 왜냐하면 코드가 디자인이고, 디자인이 코드이기 때문이다.

코드를 아무리 좋게 짜려고해도 실패한다면, 좋은 디자인인지 생각해 볼 필요가 있다.

이 챕터에서는 더 높은 추상화 수준의 디자인 원칙에 중점을 둔다. 이러한 생각은 소프트웨어 엔지니어링의 일반적인 원리이다.

고품질 코드는 다차원의 개념을 갖는다. 이것은 소프트웨어 설계의 품질 속성에 대한 고민과 비슷하다. 예를 들어 몇 가지만 말하면 안전하고 고성능이며 유지보수성이 좋기를 바라는 것이다.

이 챕터의 목표는 다음과 같다.
- 견고한 소프트웨어의 개념을 이해
- 작업 중 잘못된 데이터를 다루는 방법
- 새로운 요구 사항을 쉽게 받아들이고 확장할 수 있는 유지보수가 쉬운 소프트웨어 설계
- 개발팀의 생산성을 높이는 효율적인 코드 작성