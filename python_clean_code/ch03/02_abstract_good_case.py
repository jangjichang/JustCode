import time
import logging


class DataTransport:
    """추상화 수준에 따른 예외 분리를 한 객체의 예제"""

    retry_threshold: int = 5
    retry_n_times: int = 3

    def __init__(self, connector):
        self._connector = connector
        self.connection = None

    def deliver_event(self, event):
        self.connection = connect_with_retry(self._connector, self.retry_n_times, self.retry_threshold)
        self.send(event)

    def connect_with_retry(self, connector, retry_n_times, retry_threshold):
        """connector와 연결을 맺는다. <retry_n_times>회 재시도.

        연결에 성공하면 connection 객체 반환
        재시도까지 모두 실패하면 ConnectionError 발생

        Args:
            connector
            retry_n_times
            retry_threshold

        Raises:
            ConnectionError: [description]

        Returns:
            [type]: [description]
        """
        for _ in range(retry_n_times):
            try:
                return connector.connect()
            except ConnectionError as e:
                logging.info("%s: 새로운 연결 시도 %is", e, self.retry_threshold)
                time.sleep(retry_threshold)

        exc = ConnectionError(f"{retry_n_times}번째 재시도 연결 실패")
        logger.exception(exc)
        raise exc

    def send(self, event):
        try:
            return self.connection.send(event.decode())
        except ValueError as e:
            logger.error(f"{event} 잘못된 데이터 포함: {e}")
