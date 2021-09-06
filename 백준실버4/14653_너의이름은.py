import sys

input = lambda: sys.stdin.readline().rstrip()

n, m, k = list(map(int, input().split()))

reads = []
nonread = []
all = list(map(chr, range(65, 65 + n)))

check = n
for _ in range(m):
    a, b = list(map(str, input().split()))
    nonread.append((a, b))

check = nonread[k - 1][0]
if int(check) == 0:
    print(-1)
    sys.exit()
reads = []
for i in range(len(nonread) - 1, k - 2 , -1):
    reads.append(nonread[i][1])
for i in range(k-1, -1, -1):
    if nonread[i][0] != nonread[i - 1][0]:
        break
    reads.append(nonread[i][1])
    reads.append(nonread[i - 1][1])
reads.append('A')
reads = set(reads)
reads = list(reads)

answer = []
for i in range(len(all)):
    if all[i] not in reads:
        answer.append(all[i])
answer.sort()

print(' '.join(f'{i}' for i in answer))
