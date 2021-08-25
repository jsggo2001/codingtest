# 모험가가 모험을 떠나지 않아도 됨 무조건 많은 팀을 보내는 것이 목적

N = input()
hero = []
hero = list(map(int, input().split()))

print(N)
print(hero)

M = max(hero)
count = 0
K = (len(hero) // M) + 1
final = []

for j in range(0, K):
    lck = []
    for i in range(0, len(hero)):
        if hero[i] <= M and count < M:
            lck.append(hero[i])
            count += 1
    final.append(lck)
    index = []
    for h in range(0, len(lck)):
        for m in range(0, len(hero)):
            if hero[m] == lck[h]:
                index.append(m)
                break
    for v in range(0, len(index)):
        hero[v] = -1
    hero.remove(-1)

print(final)
