import time
N,K = map(int,input().split())
chk = 0

start = time.time()

while(True):
    if N > 1:
        if N % K == 0:
            N /= K
            chk += 1
        elif N % K !=0:
            chk += N % K
            N -= N % K
    else:
        break

if N == 0:
    chk -= 1

print(f"정답 {chk}")

end = time.time()
print(end - start)