import sys

n = int(sys.stdin.readline())
lst = []
for i in range(n):
    lst.append(list(map(int, sys.stdin.readline().split())))
    lst[i].append(i+1)
lst.sort(key=lambda x : x[2],reverse=True)
lst.sort(key=lambda x : x[1],reverse=True)
lst.sort(key=lambda x : x[0])

print(lst[len(lst)-1][3])
