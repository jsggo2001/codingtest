n = int(input())
answer = 0
for i in range(1, n + 1):
    num = str(i)
    check = []
    for j in range(1, len(num)):
        a = int(num[j - 1]) - int(num[j])
        if a not in check:
            check.append(a)
    if len(check) <= 1:
        answer += 1
print(answer)