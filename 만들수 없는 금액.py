# M = input()
# 코드 구현 아직 안함 타겟과 x 값을 이용 한 비교
# 접근방식이 아예 틀림

def solution(num):
    money = list(map(int, num.split()))
    mv = max(money)
    possible = []
    money.sort()

    for i in range(1, mv + 1):
        target = i
        check = False
        for a in money:
            i = i - a
            if i == 0:
                check = True
                break
        if check == True:
            possible.append(target)

    # print(possible)
    answer = possible

    return answer


print(solution("3 2 1 1 9"))
