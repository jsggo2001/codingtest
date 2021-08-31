import sys

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

lst = []
for i in range(n):
    lst.append([*map(str, input().rstrip())])

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

check = 1
for i in range(n):
    for j in range(m):
        if lst[i][j] == '.':
            lst[i][j] = 'D'
        elif lst[i][j] == 'W':
            for z in range(4):
                if i + dx[z] >= 0 and i + dx[z] < n and j + dy[z] >= 0 and j + dy[z] < m:
                    if lst[i + dx[z]][j + dy[z]] == "S":
                        check = 0

if check == 1:
    print(check)
    for i in range(n):
        for j in range(m):
            print(lst[i][j], end='')
        print()
else:
    print(check)
