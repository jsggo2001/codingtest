n, m = list(map(int, input().split()))
lst = list(map(int, input().split()))
d = [[]] * n
count = 0
for i in range(0, n):
    d[i] = []
    for j in range(0, m):
        d[i].append(lst[count])
        count += 1

for i in range(1, m):
    for j in range(0, n):
        val = d[j][i]
        if j == 0:
            d[j][i] = max(d[j][i - 1] + val, d[j + 1][i - 1] + val)
        elif j == n - 1:
            d[j][i] = max(d[j][i - 1] + val, d[j - 1][i - 1] + val)
        else:
            d[j][i] = max(d[j][i - 1] + val, d[j - 1][i - 1] + val, d[j + 1][i - 1] + val)
result = []
for i in range(n):
    result.append(d[i][m-1])
print(max(result))
