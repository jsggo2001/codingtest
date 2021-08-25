m, n = map(int, input("행과 열을 입력해 주세요 ").split())
print("{0} {1}".format(m, n))

min_list = []

for i in range(0, m):
    num_list = list(map(int, input("배열 값을 입력해 주세요 ").split()))
    num_list.sort()
    print(num_list)
    print(num_list[0])
    min_list.append(num_list[0])

print(min_list)
min_list.sort()
print(f"정답 {min_list[-1]}")

min(min_list)
