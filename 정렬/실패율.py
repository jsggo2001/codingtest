import sys

N = int(sys.stdin.readline())
stages = list(map(int, sys.stdin.readline().split()))

def solution(N, stages):
    rate = []
    answer = []
    length = len(stages)
    for i in range(1,N+1):
        count = stages.count(i)
        if length == 0:
            fail = 0
        else:
            fail = count / length
        answer.append((i, fail))
        length -= count
    answer.sort(key=lambda x: (-x[1], x[0]))
    answer = [i[0] for i in answer]
    return answer


print(solution(N, stages))
