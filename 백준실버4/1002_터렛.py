import sys

input = sys.stdin.readline

n = int(input())

for i in range(n):
    lst = list(map(int, input().split()))
    x1 = lst[0]
    y1 = lst[1]
    r1 = lst[2]
    x2 = lst[3]
    y2 = lst[4]
    r2 = lst[5]

    if x1 == x2 and y1 == y2:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    else:
        d = (((x1 - x2) ** 2) + ((y1 - y2) ** 2)) ** (1 / 2)

        if abs(r1 - r2) < d < abs(r1 + r2):
            print(2)
        elif r1 + r2 == d:
            print(1)
        elif abs(r1 - r2) == d:
            print(1)
        else:
            print(0)
