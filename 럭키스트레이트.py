input = input()
d = len(input)
a = 0
b = 0

for i in range(0, len(input)):
    if i <= (len(input)//2)-1:
        a += int(input[i])
    elif i > (len(input)//2)-1:
        b += int(input[i])
print(map(int, input[d:]))
if a == b:
    print("LUCKY")
else:
    print("READY")

