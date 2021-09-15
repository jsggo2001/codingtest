n = int(input())

lst = []
for i in range(n):
    lst.append(int(input()))

d = [0] * (n + 1)

d[0] = lst[0]
d[1] = lst[1]
d[2] = max(lst[1] + lst[2], lst[0] + lst[2])

for i in range(3, n):
    d[i] = max(lst[i] + d[i - 2], lst[i] + lst[i - 1] + d[i - 3])

print(d[n-1])
