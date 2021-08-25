import sys

n, c = list(map(int, input().split()))
lst = []
for _ in range(n):
    lst.append(int(sys.stdin.readline().rstrip()))
lst.sort()
start = 1
end = lst[-1] - lst[0]
result = 0
while start <= end:
    count = 1
    mid = (start + end) // 2
    val = lst[0]
    for i in range(1, n):
        if lst[i] >= val + mid:
            val = lst[i]
            count += 1
    if count >= c:
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)
