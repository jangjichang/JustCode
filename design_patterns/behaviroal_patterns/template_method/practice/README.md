# what is?
알고리즘의 구조를 메소드에 정의하고 하위 클래스에
알고리즘 구조의 변경없이 알고리즘을 재정의 하는 패턴

# when to use?
구현하려는 알고리즘이 일정한 프로세스가 있다.
- 구현하려는 알고리즘이 변경 가능성이 있다.

# how to implement?
- 알고리즘을 여러 단계로 나눈다.
- 나눠진 알고리즘의 단계를 메소드로 선언한다.
- 알고리즘을 수행할 템플릿 메소드를 만든다.
- 하위 클래스에서 나눠진 메소드들을 구현한다.

---

# 예제
## 요구사항
- 신작 게임의 접속을 구현한다.
  - request_connection(str) -> str
- 유저가 게임 접속 시 다음을 고려해야합니다.
  - 보안 과정: 보안 관련 부분을 처리합니다.
    - do_security(str) -> str
  - 인증 과정: user name과 password가 일치하는지 확인
    - authentication(id: str, password: str) -> bool
  - 권한 과정: 접속자가 유료 회원인지 무료회원인지 게임 마스터인지 확인합니다.
    - authorization(user_name: str) -> int
  - 접속 과정: 접속자에게 커넥션 정보를 넘겨줍니다.
    - connection(str) -> str
