from collections import deque

import sys

n = int(sys.stdin.readline())
lst = []
for _ in range(n):
    lst.append(int(sys.stdin.readline()))
possible = []
# lst = [6, 9, 7, 6, 4, 6]
a = lst[len(lst) - 1]
lst1 = set(lst)
lst = list(lst1)
lst.sort()
lst.reverse()
print(lst)
print(lst.index(a)+1)
# b = 0
# while q:
#     a = q.pop()
#     if a > b:
#         possible.append(a)
#         b = a
# count = 0
# b = 0
# z = max(lst)
# for i in range(len(lst)-1, -1, -1):
#     if lst[i] > b:
#         count += 1
#         b = lst[i]
#         if b == z:
#             break


# print(count)
