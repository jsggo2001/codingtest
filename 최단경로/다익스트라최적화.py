import heapq
import sys
input = sys.stdin.readline

INF = int(1e9)

n, m = map(int, input().split())

start = int(input())

graph = [[] for i in range(n + 1)]

distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    graph[a].append((b, c))


def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


# 다익스트라 알고리즘을 수행
dijkstra(start)

# 모든 노드로 가기 위한
for i in range(1, n + 1):
    # 도달할 수 없는 경우, 무한이라고 출력
    if distance[i] == INF:
        print("무한")
    # 도달할 수 있는 경우 거리를 출력
    else:
        print(distance[i])

