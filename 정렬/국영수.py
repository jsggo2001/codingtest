import sys

n = int(sys.stdin.readline())
lst = []
for i in range(n):
    lst.append(list(map(str, sys.stdin.readline().split())))

lst.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))


print(lst)
