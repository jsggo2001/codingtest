from itertools import combinations
#실패-------------------------------------------------
def solution(s):
    answer = 0
    c = []
    d = []
    for i in range(len(s)//2):
        w = set(combinations(s, i+1))
        com = list(w)
        c.append(len(com))
        d.append(com)
    print(d[7])
    print(d[c.index(min(c))])

    return answer

print(solution("ababcdcdababcdcd"))