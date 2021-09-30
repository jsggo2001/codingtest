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

print(solution([1,1,1,2,2,2,3,3,5,4,2,1,2,9,8]))
