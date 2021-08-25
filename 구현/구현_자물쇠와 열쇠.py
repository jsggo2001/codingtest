from itertools import product


# 회전 펑션들
def rotate_90(m):
    N = len(m)
    ret = [[0] * N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            ret[c][N - 1 - r] = m[r][c]
    return ret


def rotate_180(m):
    N = len(m)
    ret = [[0] * N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            ret[N - 1 - r][N - 1 - c] = m[r][c]
    return ret


def rotate_270(m):
    N = len(m)
    ret = [[0] * N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            ret[N - 1 - c][r] = m[r][c]
    return ret


M = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
N = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
keys = [M, rotate_90(M), rotate_180(M), rotate_270(M)]

# 비교하기
for i in range(0, len(N)):
    for j in range(0, len(N)):
        if N[i][j] == 0:
            N[i][j] = 1
        else:
            N[i][j] = 0

# 이동하는 인덱스 만들기
a = []
for i in range(len(M)):
    a.append(i)
    a.append(-i)
a.remove(0)
fair = list(product(a, a))
print(fair)


# 키를 타겟으로 이동

# 하나의 키로 나오는 타겟 수
def move(fair, key):
    targets = []
    fair = [(-1,-1)]
    for z in range(len(fair)):
        target = [[0 for col in range(len(M))] for row in range(len(M))]
        for i in range(len(target)):
            for j in range(len(target)):
                if i + fair[z][0] < len(target) and j + fair[z][1] < len(target):
                    target[i][j] = key[i + fair[z][0]][j + fair[z][1]]
                else:
                    target[i][j] = 0
        targets.append(target)
    return targets


# print(len(fair))

# 키 값과 매치해서 함
compare = []
for i in range(len(keys)):
    # print(i)
    compare.extend(move(fair, keys[i]))
print(compare)

print(N)
# 마지막 비교
result = False
for i in range(len(compare)):
    if N == compare[i]:
        result = True
print(result)

