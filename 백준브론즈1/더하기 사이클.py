a = int(input())
n = a
count = 0
while True:
    if len(str(n)) == 1:
        n = ((n%10)*10) + n
        count += 1
    elif len(str(n)) != 1:
        n = ((n%10)*10) + (((n//10) + (n%10))%10)
        count += 1
    if n == a:
        break

print(count)

