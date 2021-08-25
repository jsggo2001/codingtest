import sys

n, m = list(map(int, sys.stdin.readline().split()))
trees = list(map(int, sys.stdin.readline().split()))
start = 1
end = max(trees)
while start <= end:
    mid = (start + end) // 2
    result_list = [tree-mid if tree>mid else 0 for tree in trees]
    result = sum(result_list)
    if result >= m:
        start = mid + 1
    else:
        end = mid - 1
print(end)
