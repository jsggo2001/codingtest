lst = [True] * 10001
lst[0] = False

for i in range(1, 10001):
    val = i
    a = str(val)
    next = 0
    for j in range(len(a)):
        next += int(a[j])
    next += val
    if next < 10001:
        lst[next] = False
for i in range(10001):
    if lst[i] == True:
        print(i)
