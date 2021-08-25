import sys

n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))

lst.sort()

print(lst[(n-1)//2])

# allsum = []
# for i in lst:
#     sum = 0
#     for j in range(len(lst)):
#         if i >= lst[j]:
#             sum += i - lst[j]
#         else:
#             sum += lst[j] - i
#     allsum.append(sum)
# print(lst[allsum.index(min(allsum))])
