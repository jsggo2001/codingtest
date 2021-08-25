import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    result = 'NO'
    list = deque(sys.stdin.readline().rstrip())
    stack = []
    a = list.popleft()
    stack.append(a)
    while list:
        if stack:
            now = list.popleft()
            if now == '(':
                stack.append(now)
            elif now == ')':
                pre = stack.pop()
                if pre == '(':
                    result = 'YES'
                else:
                    stack.append(pre)
                    stack.append(now)
        else:
            now = list.popleft()
            stack.append(now)

    if len(stack) > 0:
        result = 'NO'
    print(result)