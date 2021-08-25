from bisect import bisect_left, bisect_right

a = [1,3,5,7,9]

b = 2

right_index = bisect_right(a, b)
if a[right_index-1] == b:
    print(1)
else:
    print(0)