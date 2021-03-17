# 기본 품질 향상을 위한 도구 설정

동료가 작성한 코드를 살펴 볼때 할 질문들
1. 이 코드를 동료 개발자가 쉽게 이해하고 따라갈 수 있을까?
2. 업무 도메인에 대해서 말하고 있는가?
3. 팀에 새로 합류하는 사람도 쉽게 이해하고 효과적으로 작업할 수 있을까?

코드 포매팅, 일관된 레이아웃, 적절한 들여쓰기를 검사하는 것만으로는 충분하지 않다.

이런 것들은 자동으로 검사하고 실제 어떤 패턴이 사용되었는지 살펴서
코드의 실제 의미와 가치를 이해하는데 시간을 투자하는 것이 효과적이다.

따라서 이 모든 검사는 자동화해야한다. 이것이 코드 구조의 연속성을 확보할 수 있는 유일한 방법이다.

이것은 팀에서 참고할 수 있는 객관적인 지표 역할도 한다. 빌드 시 자동으로 실패하도록 해야 객관성을 얻을 수 있다.

## Mypy를 사용한 타입 힌팅

정적 타입 검사 도구이다.

> pip install mypy

완벽한 도구는 아니어서 가끔 잘못된 탐지를 할 경우가 있다.
이런 경우 다음과 같이 문장 끝에 주석을 추가하여 mypy가 무시하도록 할 수 있다.

```python
type_no_ignore = "something" # type: ignore
```

## Pylint를 사용한 코드 검사

> pip install pylint

그 다음에 커맨드 창에서 pylint를 입력하기만 하면 된다.
.pylintrc 파일을 통해 설정 값을 변경할 수 있다.

## 자동 검사 설정

리눅스 개발환경에서 빌드를 자동화하는 가장 일반적인 방법은 makefile을 사용하는 것이다.

**Makefile**은 프로젝트를 컴파일하고 실행하기 위한 설정을 도와주는 파워풀한 도구이다.

빌드외에도 포매팅 검사나 컨벤션 검사를 자동화하기 위해 사용할 수도 있다.

```
typehint:
mypy src/ tests/

test:
pytest tests/

lint:
pylint src/ tests/

checklist: lint typehint test

.PHONY: typehint test lint checklist
```

이제 개발 머신과 CI 빌드 머신에서 실행할 커맨드는 다음과 같다.

> make checklist

이것은 다음 단계를 실행한다.
1. 코딩 가이드라인 검사 (예를 들면 PEP-8)
2. 올바른 타입을 사용했는지 검사
3. 최종적으로 테스트 실행

앞서 언급한 Black, Pylint, Mypy와 같은 도구들을 에디터나 IDE에 통합하여 작업을 훨씬 수월하게 할 수 있다.

파일을 저장할 때 또는 바로 가기를 통해 수정 작업을 하도록 설정하면 매우 편리하다.

## 보완할 부분들

### mac에서 makefile 에러 발생

> make checklist

make 명령어 입력시

> xcrun: error: invalid active developer path (/Library/Developer/CommandLineTools), missing xcrun at: /Library/Developer/CommandLineTools/usr/bin/xcrun

이러한 에러가 발생한다면 맥에서 제공하는커맨드 라인 유틸리티를 설치하자.

> xcode-select --install

### pylint 설정 값 변경하기
