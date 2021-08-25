import sys

caseNum = int(sys.stdin.readline().rstrip())
cases = []
for i in range(caseNum):
    case = []
    n, z = list(map(int, sys.stdin.readline().rstrip().split()))
    x = list(map(int, sys.stdin.readline().rstrip().split()))
    y = list(map(int, sys.stdin.readline().rstrip().split()))
    pan = list(map(int, sys.stdin.readline().rstrip().split()))
    case.append(x)
    case.append(y)
    case.append(pan)
    case.append(z)
    case.append(n)
    cases.append(case)


def solution(x, y, pan, z, n):
    count = 0
    small = 0
    big = 0
    l = 0
    for i in range(len(x), 0, -1):
        a = x[l] * 10 ** (i - 1)
        small += a
        l += 1
    k = 0
    for j in range(len(y), 0, -1):
        a = y[k] * 10 ** (j - 1)
        big += a
        k += 1
    pan = pan * 2
    for o in range(n):
        m = 0
        for j in range(z, 0, -1):
            m += pan[o + (z - j)] * (10 ** (j - 1))
        if small <= m <= big:
            count += 1
    return count


answer = []
for i in range(len(cases)):
    answer.append(solution(cases[i][0], cases[i][1], cases[i][2], cases[i][3], cases[i][4]))
for i in answer:
    print(i)
