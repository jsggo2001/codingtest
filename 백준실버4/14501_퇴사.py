import sys

input = sys.stdin.readline

n = int(input().rstrip())

vals = [(0, 0)] * (n + 1)

costs = [0] * (n + 1)

for i in range(1, n + 1):
    vals[i] = tuple(map(int, input().split()))

for i in range(1, len(vals)):
    day, cost = vals[i]
    premax = 0
    for j in range(1, i):
        premax = max(costs[j], premax)

    if (i - 1) + day < n+1:
        costs[(i - 1) + day] = max(costs[(i - 1) + day], cost + premax)

print(max(costs))
