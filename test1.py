def factorial_recursive(n):
    return n + factorial_recursive(n-1) if n > 1 else 1
print(factorial_recursive(5))

def factorial_recursive1(n):
    if n > 1:
        return n + factorial_recursive(n-1)
    else:
        return 1
print(factorial_recursive1(5))
