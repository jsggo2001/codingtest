n = int(input())
score = list(map(int,input().split()))
m = max(score)
sum = 0
for i in score:
    val = i / m*100
    sum += val

print(sum/n)
