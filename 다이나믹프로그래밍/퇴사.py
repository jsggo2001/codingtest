n = int(input())
lst = []
for i in range(n):
    lst.append(list(map(int, input().split())))
d = [0] * n
d[0] = 0
for j in range(0, n):
    start = j + (lst[j][0] - 1)
    comp = []
    pre = 0
    if j >= 1:
        for z in range(j):
            comp.append(d[z])
        pre = max(comp)
    if start < n:
        d[start] = max(d[start], pre + lst[j][1])
print(max(d))
