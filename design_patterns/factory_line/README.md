이런 시스템을 만들어야합니다.

입력 -> [ 바텀 시트 공장 ] -> 출력

바텀 시트 만드는 공장에 들어가면 입력 조건을 보고 물건(바텀 시트)을 뚝딱 만들어줍니다.

바텀 시트 공장은 다음과 같은 조건을 가지고 있습니다.

입력: Context
- account_id
- user_id
- target_datetime
- 이 외에 어떤 필드도 추가될 수 있음

출력: List[BottomSheet]

BottomSheet
- title
- message
- highlight
- image_url
- List[Button]

Button
- text
- url
- type

---

이걸 어떻게 만들지...
바텀 시트는 그 자체로 완성 시키면 될 것이고

그걸 체크하는게 필요한데
그걸 어떻게 해야할까

일단은 바텀 시트를 만들어보자
바텀 시트에 context가 필요한 경우도 있으니, context는 받도록 하고

체크하는 방식을 생각해보자

공장은 프로덕션 라인으로 구성되어있다.
프로덕션 라인은 컨디션 체커 컴포넌트와 바텀 시트 컴포넌트로 구성되어있다.


팩토리를 만들 때 프로덕션 라인을 주입받도록 하자.
생성자에서 프로덕션 라인이 주입 되지 않았다면, 모든 프로덕션 라인을 대상으로 바텀시트를 만든다.

특이 케이스에 대한 고려
팩토리에 생성자로 주입한다.
예를 들어 바텀시트를 정렬해줘야하거나 바텀시트가 하나라도 채워지면 끝내야하는 경우는 sort, limit, break 등의 옵션을 주입 받도록 하자.

----
Input: Context
Output: List[BottomSheet]

Factory
    List[ProductionLine]
        List[ConditionChecker]
        Maker
