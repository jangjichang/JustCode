def solution(N, K):
    """
    N자리 이진수 중 1을 K개 포함하면서 3의 배수인 이진수

    N자리 이진수?
    한자리 이진수 0~1
    두자리 이진수 0~3
    세자리 이진수 0~7
    N자리 이진수 0~2^N-1 (십진수로 표현하면)

    시간 복잡도 2^N
    N^2
    nlogn
    N

    """
    answer = 0

    for n in range(0, 2**N):
        if n % 3 == 0 and bin(n)[2:].count("1") == K:
            answer += 1

    return answer


def test_solution():
    assert solution(3, 2) == 2
    assert solution(4, 2) == 4
    assert solution(6, 3) == 2
