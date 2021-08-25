input()
ball = list(input().split())
pair = []


def solution(ball):
    first = 0
    for i in range(0, len(ball)):
        for j in range(first, len(ball)):
            if ball[i] == ball[j]:
                continue
            elif ball[i] != ball[j]:
                val = [ball[i], ball[j]]
                pair.append(val)
        first += 1
    return len(pair)

print(solution(ball))

