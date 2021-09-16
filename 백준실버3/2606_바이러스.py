n = int(input())

m = int(input())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = list(map(int, input().split()))
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)
visited[0] = True


def dfs(graph, node, visited, cnt):
    visited[node] = True
    for i in graph[node]:
        if not visited[i]:
            cnt = dfs(graph, i, visited, cnt + 1)
    return cnt

print(dfs(graph, 1, visited, 0))
