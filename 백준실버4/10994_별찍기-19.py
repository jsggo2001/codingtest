def add_star(now):
    return '* ' + now + ' *'


def star(n):
    if n == 1:
        return ['*']
    else:
        b = []
        b.append('*' * ((4 * (n-1)) + 1))
        b.append('*' + (' ' * (4 * (n-1) - 1)) + '*')
        b.extend(list(map(add_star, star(n - 1))))
        b.append('*' + (' ' * (4 * (n-1) - 1)) + '*')
        b.append('*' * ((4 * (n-1)) + 1))
        return b


answer = star(int(input()))
print('\n'.join(f'{i}' for i in answer))
