import sys

n = int(sys.stdin.readline().rstrip())
products = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(sys.stdin.readline().rstrip())
want = list(map(int, sys.stdin.readline().rstrip().split()))

products.sort()

# 이진 탐색 트리(재귀함수)
def search_want(products, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if products[mid] == target:
        return mid
    elif products[mid] > target:
        return search_want(products, target, start, mid - 1)
    else:
        return search_want(products, target, mid + 1, end)


for i in want:
    answer = search_want(products, i, 0, n - 1)
    if None != answer:
        print('yes', end=' ')
    if None == answer:
        print('no', end=' ')
