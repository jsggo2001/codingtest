a = str(input())

if len(a) == 1:
    if int(a) < 9:
        print(int(a) + 1)
    else:
        print(11)
elif len(str(int(a) + 1)) > len(a):
    print(int(a) + 2)
else:
    if len(a) % 2 == 0:
        c = ''
        for i in range(len(a) // 2 - 1, -1, -1):
            c += a[i]
        c = int(c)
        d = int(a[len(a) // 2:len(a)])
        if c <= d:
            target = []
            c = int(a[0:len(a)//2])
            c += 1
            c = str(c)
            for i in range(0, len(c)):
                target.append(c[i])
            for j in range(len(c) - 1, -1, -1):
                target.append(c[j])
        else:
            target = []
            for i in range(0, len(a) // 2):
                if i != len(a) // 2 - 1:
                    target.append(a[i])
                else:
                    target.append(str(int(a[i])))
            for i in range(len(a) // 2 - 1, -1, -1):
                if i != len(a) // 2 - 1:
                    target.append(a[i])
                else:
                    target.append(str(int(a[i])))
    else:
        c = ''
        for i in range(len(a) // 2 - 1, -1, -1):
            c += a[i]
        c = int(c)
        d = int(a[len(a) // 2 + 1:len(a)])
        if c <= d:
            target = []
            if a[len(a) // 2] == '9':
                target = []
                c = int(a[0:(len(a) // 2)])
                c += 1
                c = str(c)
                for i in range(0, len(c)):
                    target.append(c[i])
                target.append(0)
                for j in range(len(c) - 1, -1, -1):
                    target.append(c[j])
            else:
                for i in range(0, len(a) // 2 + 1):
                    if i != len(a) // 2:
                        target.append(a[i])
                    else:
                        target.append(str(int(a[i]) + 1))
                for i in range(len(a) // 2 - 1, -1, -1):
                    target.append(a[i])
        else:
            target = []
            for i in range(0, len(a) // 2 + 1):
                if i != len(a) // 2:
                    target.append(a[i])
                else:
                    target.append(str(int(a[i])))
            for i in range(len(a) // 2 - 1, -1, -1):
                target.append(a[i])

    print(''.join(f'{i}' for i in target))
