n, k = list(map(int, input().split()))

d = [[]] * 31

d[1] = [1]
d[2] = [1,1]
d[3] = [1,2,1]

for i in range(3,n+1):
    d[i] = [1] * i
    for j in range(1,i-1):
        d[i][j] = (d[i-1][j-1]) + (d[i-1][j])
print(d[n][k-1])
