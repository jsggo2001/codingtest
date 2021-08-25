from itertools import combinations

coin = [3, 2, 1, 1, 9]
cases = []
for i in range(1, len(coin) + 1):
    lst = set(map(sum, list(combinations(coin, i))))
    lst1 = list(lst)
    cases.append(lst1)
final = cases[0]
for i in range(1, len(cases)):
    final.extend(cases[i])
    final.sort()

final = list(set(final))

print(final)
