n, m = map(int, input().split())

lst = []

for _ in range((n * 5) + 1):
    lst.append([*map(str, input())])

whole_num = n * m
check_lst = []
check_lst.append(['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'])
check_lst.append(['*', '*', '*', '*', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'])
check_lst.append(['*', '*', '*', '*', '*', '*', '*', '*', '.', '.', '.', '.', '.', '.', '.', '.'])
check_lst.append(['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '.', '.', '.', '.'])
check_lst.append(['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'])

# 행 수와 컬럼수를 계산하여 넣어 주기
row, col = [], []
for m in range(m):
    row.append(5 * m + 1)
for n in range(n):
    col.append(5 * n + 1)

result = []
count = 0
while count != whole_num:
    for r in col:
        for c in row:
            temp = []
            temp.extend(lst[r][c:c + 4])
            temp.extend(lst[r + 1][c:c + 4])
            temp.extend(lst[r + 2][c:c + 4])
            temp.extend(lst[r + 3][c:c + 4])
            result.append(temp)
            count += 1

answer = []
for j in check_lst:
    answer.append(result.count(j))
print(' '.join(f'{i}' for i in answer))
