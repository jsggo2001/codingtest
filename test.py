from bisect import bisect_left, bisect_right

a = [(1, 5), (2, 4), (3, 3), (4, 2), (5, 1)]

a.sort(key = lambda x : -x[1])

print(a)

