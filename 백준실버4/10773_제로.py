import sys

n = int(sys.stdin.readline())
stack = []
for _ in range(n):
    x = int(sys.stdin.readline())
    if x != 0:
        stack.append(x)
    else:
        stack.pop()
print(sum(stack))