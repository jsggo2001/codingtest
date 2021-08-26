import sys

input = sys.stdin.readline
n = int(input().rstrip())
lst = []
for i in range(n):
    prelst = list(map(str, input().rstrip().split()))
    lst.append([prelst[0], int(prelst[1]), int(prelst[2]), int(prelst[3])])

lst.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))
for i in range(len(lst)):
    print(lst[i][0])
