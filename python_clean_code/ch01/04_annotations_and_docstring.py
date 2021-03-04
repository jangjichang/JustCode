"""
response의 status값이 기댓값과 다를 경우 예외가 발생한다. 그러나 상세한 내용은 알 수가 없다.
예를 들어, response 객체의 올바른 인스턴스는 어떤 형태일까? 결과의 인스턴스는 어떤 형태일까?
이 두가지 질문에 모두 대답하려면 파라미터와 함수 반환 값의 예상 형태를 docstring으로 문서화하는 것이 좋다.
"""

# docstring이 필요함
# def data_from_response(response: dict) -> dict:
#     if response["status"] != 200:
#         raise ValueError
#     return {"data": response["payload"]}

# 이렇게 docstring을 사용하면 위 두가지 질문도 해결되고, 테스트할 때도 입력 값을 생성할 수도 있고 테스트의 성공 실패를 판단할 수도 있다.
def data_from_response(response: dict) -> dict:
    """response에 문제가 없다면 response의 payload를 반환

    - response dict 예제:
    {
        "status": 200, # <int>
        "timestamp": "...." # 현재 시간의 ISO 포맷 문자열
        "payload": { ... } # 반환하려는 dict 데이터
    }

    - return dict 값의 예제:
    {"data": { .. } }

    - 발생 가능한 예외:
    - HTTP status가 200이 아닌 경우 ValueError 발생
    """
    if response["status"] != 200:
        raise ValueError
    return {"data": response["payload"]}
