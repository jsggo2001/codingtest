import sys

n = int(sys.stdin.readline().rstrip())
stack = []
order = []

for i in range(n):
    x = str(sys.stdin.readline().rstrip())
    a = x.split(' ')
    if len(a) > 1:
        stack.append(int(a[1]))
    else:
        if a[0] == 'pop':
            if len(stack) == 0:
                print(-1)
            else:
                s = stack.pop()
                print(s)
        elif a[0] == 'size':
            print(len(stack))
        elif a[0] == 'empty':
            if len(stack) == 0:
                print(1)
            else:
                print(0)
        elif a[0] == 'top':
            if len(stack) == 0:
                print(-1)
            else:
                print(stack[-1])
