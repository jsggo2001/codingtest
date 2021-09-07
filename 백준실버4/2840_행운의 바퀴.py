import sys

input = lambda: sys.stdin.readline().rstrip()

n, m = list(map(int, input().split()))

lst = []

for i in range(m):
    a, b = list(map(str, input().split()))
    lst.append((a, b))

answer = [''] * (n + 1)

answer[1] = lst[m - 1][1]
first = 1

for j in range(m - 1, 0, -1):
    next = (first + int(lst[j][0])) % n
    if next == 0:
        next = n
    if answer[next] == '':
        answer[next] = lst[j - 1][1]
    elif answer[next] == lst[j - 1][1]:
        first = next
        continue
    else:
        print('!')
        sys.exit()
    first = next
check = True

checklst = []

for l in answer:
    if l not in '':
        checklst.append(l)

if len(checklst) == len(set(checklst)):
    check = True
else:
    check = False
if check:
    for z in range(1, len(answer)):
        if answer[z] != '':
            print(answer[z], end='')
        else:
            print('?', end='')
else:
    print('!')