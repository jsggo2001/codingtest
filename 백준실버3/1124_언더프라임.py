def prime_list(n):
    # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    sieve = [True] * n

    # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:  # i가 소수인 경우
            for j in range(i + i, n, i):  # i이후 i의 배수들을 False 판정
                sieve[j] = False

    # 소수 목록 산출
    return sieve


x, y = list(map(int, input().split()))

list = prime_list(y + 1)
list[1] = False

answer = [0 for _ in range(y + 1)]
for i in range(1, y + 1):
    if list[i]:
        answer[i] = 1
for i in range(2, y + 1):
    for j in range(2, y + 1):
        if i * j > y:
            break
        if list[j]:
            answer[i * j] = answer[i] + 1
cnt = 0

for i in range(x, y + 1):
    if list[answer[i]]:
        cnt += 1
print(cnt)
