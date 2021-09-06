import sys

input = lambda: sys.stdin.readline().rstrip()

target = [*map(str, input())]

target1 = set(target)

target2 = list(target1)

targetdic = {}

for i in target2:
    targetdic[i] = 0

for j in target:
    targetdic[j] += 1
targetdic = sorted(targetdic.items())

answer1 = []
check = 0
middle = ''
for i in range(len(targetdic)):
    if targetdic[i][1] % 2 != 0:
        check += 1
        if check == 1:
            middle = targetdic[i][0]
        for z in range(targetdic[i][1]//2):
            answer1.append(targetdic[i][0])
    else:
        for z in range(targetdic[i][1]//2):
            answer1.append(targetdic[i][0])
answer2 = list(reversed(answer1))

if check < 2:
    for i in answer1:
        print(i, end='')
    print(middle, end='')
    for j in answer2:
        print(j, end='')
else:
    print("I'm Sorry Hansoo")
