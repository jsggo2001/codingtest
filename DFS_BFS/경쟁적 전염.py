# 1 넣었을때 되야 됨
# 원래답 보고 한번 더 풀기
n, m = map(int, input().split())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))
g, l, y = map(int, input().split())

# 4가지 이동 방향에 대한 리스트
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0

# 바이러스의 위치 뽑기
position = [[] for _ in range(m)]

virus = [i+1 for i in range(m)]

for x in range(len(virus)):
    for i in range(n):
        for j in range(n):
            if data[i][j] == virus[x]:
                position[x].append([i,j])


# 깊이 우선 탐색(DFS)을 이용해 각 바이러스가 사방으로 퍼지도록 하기
def virus(x, y ,v):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 상, 하, 좌, 우 중에서 바이러스가 퍼질 수 있는 경우
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if data[nx][ny] == 0:
                # 해당 위치에 바이러스 배치 하고, 다시 재귀적으로 수행
                data[nx][ny] = v
count = 0
# 바이러스를 시간 많큼 퍼트리기
while(True):
    if count == g:
        break

    for i in range(len(position)):
        for j in range(len(position[i])):
            virus(position[i][j][0], position[i][j][1], i+1)

    count += 1
    virus2 = [i + 1 for i in range(m)]
    position = [[] for _ in range(m)]
    for x in range(m):
        for i in range(n):
            for j in range(n):
                if data[i][j] == virus2[x]:
                    position[x].append([i, j])
print(data)

result = data[l-1][y-1]

print(result)