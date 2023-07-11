# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение дробей. Для проверки своего кода используйте
# модуль fractions.

n = input('Enter a fraction A: ')
m = input('Enter a fraction B: ')
a = n.split('/')
b = m.split('/')
c = [a, b]
i = 0
while i < len(c):
    a[i] = int(a[i])
    b[i] = int(b[i])
    i += 1

s_res = []
if a[1] == b[1]:
    s_res = [a[0] + b[0], a[1]]
else:
    s_res = [a[0] * b[1] + b[0] * a[1], a[1] * b[1]]

m_res = [a[0] * b[0], a[1] * b[1]]

def denominator(d):
    j = 2
    if d[0] < d[1]:
        den = d[0]
    else:
        den = d[1]
        if d[0] % d[1] == 0:
            res = d[0] / d[1]
            return int(res)
    while j <= den:
        if d[0] % j == 0 and d[1] % j == 0:
            d[0] /= j
            d[1] /= j
            continue
        j += 1
    return [int(d[0]), int(d[1])]

s_res = denominator(s_res)
m_res = denominator(m_res)

def performance(d):
    if type(d) == int:
        return d
    else:
        return f'{d[0]}/{d[1]}'

sum_res = performance(s_res)
multy_res = performance(m_res)

print('Sum of fractions: {} + {} = {}'.format(n, m, sum_res))
print('Multiplication of fractions: {} * {} = {}'.format(n, m, multy_res))

import fractions
print('\nChecking with "fractions":')
x = fractions.Fraction(a[0], a[1])
y = fractions.Fraction(b[0], b[1])
print(f'{x} + {y} = {x + y}')
print(f'{x} * {y} = {x * y}')
