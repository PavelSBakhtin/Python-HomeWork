# Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
# Дано a, b, c — стороны предполагаемого треугольника. Требуется сравнить длину каждого
# отрезка-стороны с суммой двух других. Если хотя бы в одном случае отрезок окажется больше
# суммы двух других, то треугольника с такими сторонами не существует. Отдельно сообщить
# является ли треугольник разносторонним, равнобедренным или равносторонним.

import random

def triangle_check(a, b, c):
    if a+b > c and a+c > b and b+c > a:
        return True
    else:
        return False

def triangle_add(x):
    if x == 1:
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        c = random.randint(1, 100)
    elif x == 2:
        a = int(input('Enter value а: '))
        b = int(input('Enter value b: '))
        c = int(input('Enter value c: '))
    print("=" * 25)
    #return triangle_check(a, b, c)
    return a, b, c

def show_menu() -> int:
    print("\n" + " " * 8 + "Main menu")
    print("=" * 25)
    print("1. Enter values randomly")
    print("2. Enter values manually")
    print("=" * 25)
    item = int(input("Select a menu item: "))
    while item < 1 or item > 2:
        print("Input error") # ошибка ввода
        item = int(input("Select a menu item: "))
    else:
        return triangle_add(item)

def triangle_type(a, b, c):
    if a == b == c:
        return "This is an equilateral triangle" # равносторонний
    elif a == b or a == c or b == c:
        return "This is an isosceles triangle" # равнобедренный
    elif a+b > c and a+c > b and b+c > a:
        return "This is a scaled triangle" # разносторонний
    else:
        None

a, b, c, = show_menu()
print('Triangle given:\na={}, b={}, c={}\n{}'.format(a, b, c, ("=" * 25)))
print("It's a triangle" if triangle_check(a, b, c) else "It's not a triangle")
if triangle_check(a, b, c) == True:
    print(triangle_type(a, b, c))
