a = 1
b = 1

N = int(input())
input = list(input().split())

for i in input:
    if i == "L":
        if b != 1:
            b -= 1
    elif i == "R":
        if b != N:
            b += 1
    elif i == "U":
        if a != 1:
            a -= 1
    elif i == "D":
        if a != N:
            a += 1

print(f"{a} {b}")