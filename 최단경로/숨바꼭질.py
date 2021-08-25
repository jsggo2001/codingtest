import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
# 시작 노드를 1번 헛간으로 설정
start = 1
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for i in range(n + 1)]
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())
    # a번 노드와 b번 노드의 이동 비용이 1 이라는 의미(양방향)
    graph[a].append((b, 1))
    graph[b].append((a, 1))


def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(start)

max_node = 0
max_distance = 0

result = []

for i in range(1, n + 1):
    if max_distance < distance[i]:
        max_node = i
        max_distance = distance[i]
        result = [max_node]
    elif max_distance == distance[i]:
        result.append(i)
print(max_node, max_distance, len(result))
