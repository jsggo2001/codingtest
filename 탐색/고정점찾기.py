import sys


n = int(input())
lst = list(map(int, sys.stdin.readline().rstrip().split()))

start = 0
end = n
answer = -1

while start <= end:
    mid = (start + end) // 2
    if lst[mid] == mid:
        answer = mid
        break
    elif lst[mid] < mid:
        start = mid + 1
    else:
        end = mid - 1
print(answer)


