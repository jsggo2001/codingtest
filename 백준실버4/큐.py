import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
q = deque()
order = []

for i in range(n):
    x = str(sys.stdin.readline().rstrip())
    a = x.split(' ')
    if len(a) > 1:
        q.append(int(a[1]))
    else:
        if a[0] == 'pop':
            if len(q) == 0:
                print(-1)
            else:
                s = q.popleft()
                print(s)
        elif a[0] == 'size':
            print(len(q))
        elif a[0] == 'empty':
            if len(q) == 0:
                print(1)
            else:
                print(0)
        elif a[0] == 'front':
            if len(q) == 0:
                print(-1)
            else:
                print(q[0])
        elif a[0] == 'back':
            if len(q) == 0:
                print(-1)
            else:
                print(q[-1])

