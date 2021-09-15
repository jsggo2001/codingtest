m = int(input())
n = 11
d = [0] * (n + 1)

d[1] = 1
d[2] = 2
d[3] = 4

for i in range(4, n + 1):
    d[i] = d[i - 1] + d[i - 2] + d[i - 3]

for _ in range(m):
    print(d[int(input())])
