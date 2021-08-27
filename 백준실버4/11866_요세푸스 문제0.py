from collections import deque

n, m = map(int, input().split())

lst = [i + 1 for i in range(n)]
q = deque(lst)
answer = []
cnt = 1
while q:
    if cnt != m:
        a = q.popleft()
        q.append(a)
        cnt += 1
    else:
        a = q.popleft()
        answer.append(a)
        cnt = 1

print('<', end='')
for i in range(len(answer)):
    if i != len(answer) - 1:
        print(answer[i], end=', ')
    else:
        print(answer[i], end='')

print('>', end='')
