# 아예 틀림 개 어려움 4레벨 천천히 보기
def solution(food_times, k):
    answer = 0
    now = []
    flag = True
    i = 0
    j = 0
    while (flag):
        if food_times[j] != 0:
            food_times[j] -= 1
            now.append(j + 1)
        # elif food_times[j] == 0:
        # now.append(0)
        i += 1
        j = (j + 1) % len(food_times)
        if i == k*10:
            flag = False

    # for i in now:
    #     if i == 0:
    #         now.remove(i)
    # answer = now[k]
    return now

    # return answer


print(solution([4, 0, 4, 3], 6))
