from collections import deque

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

result = []

q = deque([[0,0]])
flag = False
while q:
    a = q.popleft()
    x = a[0]
    y = a[1]
    if graph[x][y] == 0:
        break
    if graph[x][y] == -1:
        flag = True
        break
    distance = graph[x][y]

    for i in range(2):
        if i == 0:
            z = 0
            z = x + distance
            if z < n:
                q.append([z, y])
        else:
            z = 0
            z = y + distance
            if z < n:
                q.append([x, z])
if flag:
    print("HaruHaru")
else:
    print("Hing")
