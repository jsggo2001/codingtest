import sys;
from collections import Counter

r = sys.stdin.readline

n = int(r())
carddic = Counter(list(map(int, r().rstrip().split())))
m = int(r())
target = list(map(int, r().rstrip().split()))

print(' '.join(f'{carddic[m]}' if m in carddic else '0' for m in target))
