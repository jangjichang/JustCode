class Connetor:
    """의도한 것이 아니라면 이중 밑줄을 사용하지 말자.
    속성이 다른 이름으로 존재하는 하게 된다.
    밑줄 두개를 사용하면 실제로 파이썬은 다른 이름을 만든다. 이를 이름 맹글링이라한다.
    "_<class_name>__<attribute-name>"으로 속성을 만든다.
    """

    def __init__(self, source):
        self.source = source
        self.__timeout = 60

    def connect(self):
        print(f"connecting with {self.__timeout}s")


conn = Connetor("postgresql://localhost")
conn.connect()
conn.__timeout
