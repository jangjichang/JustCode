"""
리소스 관리와 관련하여 컨텍스트 관리자를 자주 볼 수 있다.
파일을 열면 파일 디스크립터 누수를 막기 위해 작업이 끝나면 적절히 닫히길 기대한다.
또는 서비스나 소켓에 대한 연결을 열었을 때도 적절하게 닫거나 임시 파일을 제거하는 등의 작업을 해야한다.
"""

filename = "python_clean_code/ch02/test.txt"

with open(filename) as fd:
    for content in fd:
        print(content)
