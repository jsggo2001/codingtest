M = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
a = [0, 1]


def shift(lst):
    temp = lst[len(lst) - 1]
    for i in range(len(lst)-1, 0, -1):
        lst[i] = lst[i - 1]
    lst[0] = temp


print(M[1])
shift(M[1])
print(M[1])
shift(M[1])
print(M[1])
shift(M[1])
print(M[1])
shift(M[1])
print(M[1])
shift(M[1])
print(M[1])
shift(M[1])
print(M[1])
shift(M[1])
print(M[1])


