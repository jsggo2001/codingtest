n, m = map(int, input().split())

setprice = 1001
price = 1001
for i in range(m):
    x, y = map(int, input().split())
    setprice = min(setprice, x)
    price = min(price, y)

if setprice == 0 or price == 0:
    print(0)
else:
    mincount = setprice // price
    if mincount >= 6:
        answer = n * price
    else:
        answer = 0
        if n % 6 <= mincount:
            answer += (n % 6) * price
        else:
            answer += setprice

        answer += (n // 6) * setprice

    print(answer)
