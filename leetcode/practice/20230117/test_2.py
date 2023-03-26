import heapq
# 문제집 개수와 우선 순위 개수

if __name__ == '__main__':
    n, priority = map(int, input().split())

    # 진입 차수
    indegree = [0] * (n + 1)

    graph = [[] for i in range(n + 1)]

    # 우선순위로 그래프 초기화하기
    for _ in range(priority):
        first, later = map(int, input().split())
        graph[first].append(later)
        indegree[later] += 1

    queue = []
    for i in range(1, n + 1):
        if indegree[i] == 0:
            heapq.heappush(queue, i)

    while queue:
        current = heapq.heappop(queue)

        print(current, end=" ")
        for g in graph[current]:
            indegree[g] -= 1

            if indegree[g] == 0:
                heapq.heappush(queue, g)






#
# answer = []
# q = deque()
#
# for i in range(1, n + 1):
#     if indegree[i] == 0:
#         q.append(i)