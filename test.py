a = [1,2,3,4,5,6,7,8,9,10]

start = 0
end = len(a) - 1
target = 10

while True:
    mid = (start + end) // 2

    if a[mid] == target:
        print(mid)
        break
    elif a[mid] > target:
        end = mid - 1
    else:
        
        start = mid + 1



