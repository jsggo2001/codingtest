def solution(num):
    answer = 0
    count = []
    for i in range(1, len(num)):
        if num[i - 1] == num[i]:
            continue
        else:
            count.append(1)

    if len(count) % 2 == 0:
        answer = len(count) // 2
    else:
        answer = len(count) // 2 + 1

    return answer


print(solution("110011001100"))
print(solution("110011"))
print(solution("1100110000"))
print(solution("1100110001"))
print(solution("0110110000"))
print(solution("1100110011001100"))
print(solution("1010101"))
print(solution("10101011"))
