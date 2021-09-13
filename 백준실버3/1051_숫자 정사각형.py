import sys

input = lambda: sys.stdin.readline().rstrip()

n, m = list(map(int, input().split()))

lst = []

for i in range(n):
    lst.append([*map(int, input())])

# 가로 체크
ans = 0
for i in range(m):
    for z in range(n):
        for j in range(1, n):
            a = j + z
            b = i + j
            if b < m and a < n:
                if lst[a][b] == lst[z][i]:
                    if lst[a][b] == lst[z][b] and lst[a][b] == lst[a][i]:
                        ans = max((j + 1), ans)
if ans == 0:
    print(1)
else:
    print(ans * ans)
