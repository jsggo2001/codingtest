import sys
from bisect import bisect_left, bisect_right


def count_by_range(lst, left_value, right_value):
    right_index = bisect_right(lst, right_value)
    left_index = bisect_left(lst, left_value)
    return right_index - left_index


n, x = list(map(int, sys.stdin.readline().rstrip().split()))
lst = list(map(int, sys.stdin.readline().rstrip().split()))

count = count_by_range(lst, x, x)

if count == 0:
    print(-1)
else:
    print(count)