import sys

n, m = list(map(int, sys.stdin.readline().split()))
trees = list(map(int, sys.stdin.readline().split()))
mids = []

# 이진 탐색(재귀함수)
def solution(trees, m, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    mids.append(mid)
    result = 0
    for i in range(len(trees)):
        a = trees[i] - mid
        if a >= 0:
            result += a
    if result == m:
        return mid
    elif result > m:
        return solution(trees, m, mid + 1, end)
    elif result < m:
        return solution(trees, m, start, mid - 1)

answer = solution(trees, m, 0, max(trees))
print(answer)
print(mids)
