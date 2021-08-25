import time


def solution(S):
    a = []
    b = []
    for i in S:
        if i.isalpha() == True:
            a.append(i)
        if i.isalpha() == False:
            b.append(int(i))
    a.sort()
    b = sum(b)
    return ''.join(a) + str(b)

start = time.time()
print(solution("K1KA5CB7" * int(1e5)))
end = time.time()
print(end - start)
print(solution("AJKDLSI412K4JSJ9D"))
