from abstract_game_connector import AbstractGameConnector


class DefaultGameConnector(AbstractGameConnector):
    def _do_security(self, string: str) -> str:
        print(f"강화된 보안 적용. {string}")
        return string

    def _authentication(self, id: str, password: str) -> bool:
        print("아이디/암호 확인 과정")
        return True

    def _authorization(self, user_name: str) -> int:
        print("권한 확인")
        # 서버에서 유저이름으로 나이를 확인하고 10시가 지났다면 성인만 통과한다.
        return 0

    def _connection(self, string: str) -> str:
        print("마지막 접속 단계")
        return string
