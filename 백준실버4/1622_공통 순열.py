while True:
    try:
        a = input()
        b = input()
        answer = []
        for i in a:
            if i in b:
                answer.append(i)
                b = b.replace(i, "", 1)
        answer.sort()
        print(''.join(answer))
    except:
        break