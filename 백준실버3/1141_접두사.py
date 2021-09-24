n = int(input())

lst = []

for i in range(n):
    lst.append(str(input()))
lst.sort(key=len)

answer = n

for i in range(len(lst)):
    for j in range(i+1, len(lst)):
        if lst[j].startswith(lst[i]):
            answer -= 1
            break
print(answer)
