import sys

input = sys.stdin.readline

n, m = list(map(int, input().rstrip().split()))

book = {}
book1 = []
for i in range(n):
    name = str(input().rstrip())
    book[name] = i
    book1.append(name)

for i in range(m):
    a = str(input().rstrip())
    if 48 <= ord(a[0]) <= 57:
        print(book1[int(int(a)-1)])
    else:
        print(book[a]+1)
