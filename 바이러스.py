n = int(input())
m = int(input())
data = []
for _ in range(m):
    data.append(list(map(int, input().split())))
map = [[] for _ in range(n+1)]
for i in range(n+1):
    for j in range(m):
        if i == data[j][0]:
            map[i].append(data[j][1])
        elif i == data[j][1]:
            map[i].append(data[j][0])
answer = []
def dfs(map, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    answer.append(v)
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in map[v]:
        if not visited[i]:
            dfs(map, i, visited)

visited = [False] * (n+1)

dfs(map,1,visited)
print(len(answer)-1)