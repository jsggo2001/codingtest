import sys
from bisect import bisect_left, bisect_right

n = int(sys.stdin.readline().rstrip())

lst = list(map(int, sys.stdin.readline().rstrip().split()))

m = int(sys.stdin.readline().rstrip())

lst1 = list(map(int, sys.stdin.readline().rstrip().split()))

lst.sort()

for i in range(m):
    right_index = bisect_right(lst, lst1[i])
    index = right_index
    origin = lst1[i]
    lstval = lst[right_index - 1]
    if lst[right_index - 1] == lst1[i]:
        print(1)
    else:
        print(0)
