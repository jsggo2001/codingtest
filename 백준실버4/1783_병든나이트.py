n, m = map(int, input().split())

answer = 1
if n == 1:
    answer = 1
elif n == 2:
    if 7 <= m:
        answer = 4
    else:
        answer = (m+1) // 2
elif n >= 3:
    if m >= 7:
        answer = m - 2
    elif 4 <= m <= 6:
        answer = 4
    else:
        answer = m
print(answer)
