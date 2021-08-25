import sys
num = 1
for _ in range(3):
    num *= int(sys.stdin.readline())
a = [0 for _ in range(10)]
for i in str(num):
    a[int(i)] += 1
for i in a:
    print(i)