n, m = list(map(int, input().split()))

lst = list(str(input()))
for i in range(len(lst)):
    lst[i] = (lst[i], 1)

lst.reverse()

lst2 = list(str(input()))
for i in range(len(lst2)):
    lst2[i] = (lst2[i], 2)
lst = lst + lst2

t = int(input())
count = 0
while True:
    if count >= t:
        break
    move = []
    for i in range(0, len(lst)):
        if i < len(lst)-1:
            if lst[i][1] < lst[i + 1][1]:
                move.append(lst[i + 1])
                move.append(lst[i])
            else:
                move.append(lst[i])
        else:
            move.append(lst[i])
    lst = []
    for v in move:
        if v not in lst:
            lst.append(v)
    count += 1
for i in range(len(lst)):
    print(lst[i][0], end='')
