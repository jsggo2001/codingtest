

def factorial_iterative(n):
    result = 1
    for i in range(1, n+1):
        print(result)
        result *= i
    return result

def factorial_recursive(n):
    if n <= 1:
        return 1
    return n*factorial_recursive(n-1)

print('반복적:', factorial_iterative(1000000))
print('재귀적:', factorial_recursive(1000000))



