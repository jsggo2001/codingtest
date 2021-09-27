import sys

input = sys.stdin.readline

n, l, w, h = list(map(int, input().split()))

start = 0
end = min(l, w, h)
for i in range(10000):
    mid = (start + end) / 2
    cnt = (l // mid) * (w // mid) * (h // mid)
    if cnt >= n:
        start = mid
    else:
        end = mid
print(mid)
