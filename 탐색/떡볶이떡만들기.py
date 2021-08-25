import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
lst = list(map(int, sys.stdin.readline().rstrip().split()))


def slice(lst, target, start, end):
    mid = 0
    while start <= end:
        mid = (start + end) // 2
        sum = 0
        for i in lst:
            a = i - mid
            if a >= 0:
                sum += i - mid
        if sum == target:
            return mid
        elif sum > target:
            start = mid + 1
        elif sum < target:
            end = mid - 1
    return mid

val = slice(lst, m, 0, max(lst))
print(val)
