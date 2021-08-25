n = int(input())

d = [10001] * 5001
array = [3, 5]
d[0]=0
for i in range(len(array)):
    for j in range(array[i], n + 1):
        if d[j - array[i]] != 10001:
            d[j] = min(d[j], d[j - array[i]] + 1)
answer = d[n]

if answer == 10001:
    print(-1)
else:
    print(answer)
