from abc import ABC, abstractmethod


class AbstractGameConnector(ABC):
    @abstractmethod
    def _do_security(self, string: str) -> str:
        raise NotImplementedError

    @abstractmethod
    def _authentication(self, id: str, password: str) -> bool:
        raise NotImplementedError

    @abstractmethod
    def _authorization(self, user_name: str) -> int:
        raise NotImplementedError

    @abstractmethod
    def _connection(self, string: str) -> str:
        raise NotImplementedError

    def request_connection(self, encoded_account_text: str) -> str:
        decoded_account_text = self._do_security(string=encoded_account_text)
        id, password, user_name = decoded_account_text.split(",")

        if not self._authentication(id=id, password=password):
            raise Exception("Authentication failed.")

        auth_group_number = self._authorization(user_name=user_name)

        if auth_group_number == -1:
            raise Exception("Authorization failed.")
        elif auth_group_number == 0:
            print("게임 매니저")
        elif auth_group_number == 1:
            print("유료 회원")
        elif auth_group_number == 2:
            print("무료 회원")
        elif auth_group_number == 3:
            print("권한 없음")

        return self._connection(string=decoded_account_text)
