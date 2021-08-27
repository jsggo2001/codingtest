import sys

input = sys.stdin.readline

def dfs(node, cnt):
    now = node
    visited[now] = True
    if len(graph[now]) > 0:
        for i in graph[now]:
            if visited[i] == False:
                cnt = dfs(i, cnt + 1)
    return cnt


for i in range(int(input())):
    n, m = map(int, input().split())
    visited = [False] * (n + 1)
    graph = [[] for _ in range(n + 1)]
    for j in range(m):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)

    print(dfs(1, 0))
