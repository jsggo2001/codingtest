a = [*map(str,input())]

print(a)

a = [1, 2, 3, 4, 5]
b = [5, 4, 3, 2, 1]

for z, c in zip(a, b):
    print(z, c)

l = [1, 2, 3, 4, 5, 6]

print(','.join(f'{i}' for i in l if (i % 3) == 0))