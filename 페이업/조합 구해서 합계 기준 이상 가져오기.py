from itertools import combinations

def solution(arr, k, t):
    answer = 0
    lst = []
    for i in range(k,len(arr)+1):
        lst.extend(list(combinations(arr, i)))
    for i in lst:
        if sum(i) <= t:
            answer += 1
    return answer
print(solution([1,1,2,2],2,3))