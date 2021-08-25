n = int(input())

d = [0] * (n + 1)

if n >= 2:
    d[0] = 0
    d[1] = 1
    for i in range(2, n + 1):
        d[i] = d[i - 1] + d[i - 2]

    answer = (d[i] * 4) + (d[i - 1] * 2)
elif n == 1:
    answer = 4

print(answer)
