import sys

input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().rstrip().split()))
m = int(input())
students = []
for _ in range(m):
    a, b = list(map(int, input().rstrip().split()))
    students.append((a, b))

for i in range(m):
    if students[i][0] == 1:
        counts = int(n / students[i][1])
        for j in range(counts):
            if lst[students[i][1] * (j + 1) - 1] == 0:
                lst[students[i][1] * (j + 1) - 1] = 1
            else:
                lst[students[i][1] * (j + 1) - 1] = 0
    else:
        idx1, idx2 = students[i][1] - 2, students[i][1]
        while True:
            if idx1 > 0 and idx2 < len(lst):
                if lst[idx1] == lst[idx2]:
                    idx1 = idx1 - 1
                    idx2 = idx2 + 1
                else:
                    idx1 = idx1 + 1
                    idx2 = idx2 - 1
                    break
            else:
                idx1 = idx1 + 1
                idx2 = idx2 - 1
                break
        for l in range(idx1, idx2 + 1):
            if lst[l] == 1:
                lst[l] = 0
            else:
                lst[l] = 1

print(' '.join(f'{i}' for i in lst))
