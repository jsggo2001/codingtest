n = int(input())
target = ['A']
count = 0
d = [0] * 46
d[0] = [1, 0]
d[1] = [0, 1]
d[2] = [1, 1]
for i in range(3, n + 1):
    d[i] = [0, 0]
    d[i][0] = d[i - 1][0] + d[i - 2][0]
    d[i][1] = d[i - 1][1] + d[i - 2][1]

print(d[n][0], d[n][1])
