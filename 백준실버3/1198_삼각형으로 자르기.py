from itertools import combinations

n = int(input())

lst = []
for i in range(n):
    a, b = list(map(int, input().split()))
    lst.append((a, b))

comlst = list(combinations(lst, 3))
ans = 0
for i in comlst:
    ans = max(abs((i[0][0] * i[1][1] + i[1][0] * i[2][1] + i[2][0] * i[0][1]) - (
                i[0][0] * i[2][1] + i[2][0] * i[1][1] + i[1][0] * i[0][1])) * 0.5, ans)

print(ans)
