import sys

lst = []

input = lambda: sys.stdin.readline().rstrip()

n, m = list(map(int, input().split()))
for i in range(n):
    lst.append(float(input()))
count = 0
lst.sort()
answer1 = 0
answer2 = 0
for i in range(m, n - m):
    answer1 += lst[i]
    if i == m or i == n - m - 1:
        for j in range(m + 1):
            answer2 += lst[i]
    else:
        answer2 += lst[i]

answer1 = answer1 / (n - (2 * m))

if n == 3:
    answer2 = 3 * lst[1] / n
else:
    answer2 = answer2 / n

print("{:.2f}".format(answer1+0.0000000001))
print("{:.2f}".format(answer2+0.0000000001))

