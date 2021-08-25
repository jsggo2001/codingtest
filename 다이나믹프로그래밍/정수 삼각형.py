n = int(input())
lst = []
for i in range(n):
    lst.append(list(map(int, input().split())))
for i in range(1, n):
    for j in range(len(lst[i])):
        val = lst[i][j]
        if j == 0:
            lst[i][j] = lst[i - 1][j] + val
        elif j == len(lst[i]) - 1:
            lst[i][j] = lst[i - 1][j - 1] + val
        else:
            lst[i][j] = max(lst[i - 1][j - 1] + val, lst[i - 1][j] + val)
result = []
for i in range(len(lst[n - 1])):
    result.append(lst[n - 1][i])
print(max(result))
