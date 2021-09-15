n = int(input())

lst = list(map(int, input().split()))

lst.sort()

d = [0] * n

d[0] = lst[0]

for i in range(1, n):
    d[i] = lst[i] + d[i-1]

print(sum(d))
