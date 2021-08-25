import sys

n = int(sys.stdin.readline().rstrip())

lst = list(map(int, sys.stdin.readline().rstrip().split()))
answer = 0
for i in lst:
    check = 0
    for j in range(1, i + 1):
        if i % j == 0:
            check += 1
    if check == 2:
        answer += 1
print(answer)
