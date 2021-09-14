import sys

input = lambda: sys.stdin.readline().rstrip()

n = int(input())

for _ in range(n):
    ans = 0

    x1, y1, x2, y2 = list(map(int, input().split()))

    m = int(input())

    lst = []
    for i in range(m):
        a, b, r = list(map(int, input().split()))
        check = 0
        if ((((a - x1) ** 2) + ((b - y1) ** 2)) ** 0.5) < r:
            check += 1
        if ((((a - x2) ** 2) + ((b - y2) ** 2)) ** 0.5) < r:
            check += 1
        if check == 1:
            ans += 1

    print(ans)
