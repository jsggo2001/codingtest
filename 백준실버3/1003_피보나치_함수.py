import sys

input = lambda: sys.stdin.readline().rstrip()

n = int(input())

# 피보나치 구하기

check = [(0, 0)] * 41

# 피보나치
check[0] = (1, 0)
check[1] = (0, 1)

for i in range(2, 41):
    check[i] = (check[i - 1][0] + check[i - 2][0], check[i - 1][1] + check[i - 2][1])

for i in range(n):
    val = int(input())
    print(check[val][0] , check[val][1])
