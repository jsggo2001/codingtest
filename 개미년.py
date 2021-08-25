import time


load = []

for i in range(0, 10):
    lst = list(map(int, input().split()))
    load.append(lst)

start = time.time()
next = 0
flag = 0
i = 0
while flag == 0:
    for j in range(next, 10):
        if load[i][j] != 2:
            if load[i][j] == 1:
                if i == 0:
                    continue
                elif j >= 1:
                    break
            elif load[i][j] == 0:
                load[i][j] = 9
                next = j
                continue
        elif load[i][j] == 2:
            load[i][j] = 9
            flag = 1
            break
    if i < len(load)-1:
        i += 1
    elif i == len(load)-1:
        flag = 1

for i in range(0, len(load)):
    for j in range(0, len(load[i])):
        print(load[i][j], end=' ')
    print()

end = time.time()
print(end - start)