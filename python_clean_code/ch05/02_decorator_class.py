from datetime import datetime


class LoginEventSerializer:
    """password 필드를 숨기고, timestamp 필드를 포매팅한다."""

    def __init__(self, event):
        self.event = event

    def serialize(self) -> dict:
        return {
            "username": self.event.username,
            "password": "**민감한 정보 삭제**",
            "ip": self.event.ip,
            "timestamp": self.event.timestamp.strftime("%Y-%m-%d %H:%M"),
        }


class LoginEvent:
    SERIALIZER = LoginEventSerializer

    def __init__(self, username, password, ip, timestamp):
        self.username = username
        self.password = password
        self.ip = ip
        self.timestamp = timestamp

    def serialize(self) -> dict:
        return self.SERIALIZER(self).serialize()


if __name__ == "__main__":
    username = "장지창"
    password = "test123"
    ip = "192.168.0.1"
    timestamp = datetime.utcnow()
    event = LoginEvent(username, password, ip, timestamp)

    print(event.serialize())
