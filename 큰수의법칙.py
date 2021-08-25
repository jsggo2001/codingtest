N = [2,4,6,5,7,8,5,1]
M = 12
K = 4

import time
start = time.time()
final = 0

a = max(N)
print(N)
N.remove(max(N))
print(N)
b = max(N)

while(True):
    if M >= K:
        final += a*K
        M -= K
        if M != 0:
            final += b
            M -= 1
        else:
            break
    elif K > M > 0:
        final += a*M
        M -= M
    elif M == 0:
        break
end = time.time()

print(end-start)
print(final)
        

 

