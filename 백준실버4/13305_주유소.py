import sys

input = sys.stdin.readline

n = int(input())
distance = list(map(int, input().rstrip().split()))
price = list(map(int, input().rstrip().split()))
answer = 0
predis = 0
preprice = price[0]
for i in range(n - 1):
    if i != n-2:
        if preprice > price[i + 1]:
            answer += preprice * (distance[i] + predis)
            preprice = price[i + 1]
            predis = 0
        else:
            predis += distance[i]
    else:
        answer += preprice * (distance[i] + predis)
        preprice = price[i + 1]
        predis = 0
print(answer)

