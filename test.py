import collections

def solution(arr):
    answer = []
    dict = collections.Counter(arr)
    for key, value in dict.items():
        if value == 1:
            answer.append(key)
    answer.sort()
    if len(answer) == 0:
        answer = [-1]
    return answer

print(solution([3, 5, 3, 5, 7, 5, 7]))
