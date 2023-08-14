# Напишите следующие функции:
# - Нахождение корней квадратного уравнения;
# - Генерация csv файла с тремя случайными числами в каждой строке (100-1000 строк);
# - Декоратор, запускающий функцию нахождения корней квадратного уравнения
#   с каждой тройкой чисел из csv файла;
# - Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.

from random import randint, choice
from functools import wraps
import json
import csv


# Корни квадратного уравнения:


def square_roots(a, b, c):
    D = b ** 2 - 4 * a * c
    if D >= 0:
        x = (-b + D ** 0.5) / (2 * a)
        y = (-b - D ** 0.5) / (2 * a)
        if x == y:
            return (f'Корень квадратного уравнения: {round(x, 2)}')
        else:
            return (f'Корни квадратного уравнения: {round(x, 2)}, {round(y, 2)}')
    else:
        return ('Квадратное уравнение не имеет корней')


# Генерация csv файла с тремя случайными числами в каждой строке (100-1000 строк):


def csv_generate():
    with open('homework9_task2.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for _ in range(randint(100, 1001)):
            writer.writerow([randint(1, 100) * choice([-1, 1]) for _ in range(3)])


# Декоратор, запускающий функцию нахождения корней квадратного уравнения
# с каждой тройкой чисел из csv файла:


def csv_to_square(func):
    @wraps(func)
    def wrapper():
        results = []
        with open('homework9_task2.csv', 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                a, b, c = map(int, row)
                results.append(func(a, b, c))
        return results
    return wrapper


# Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл:


def square_to_json(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        with open('homework9_task2.json', 'w', encoding='utf-8') as f2:
            json.dump(result, f2, indent=0, ensure_ascii=False)
        return result
    return wrapper


# Основное выполнение программы:

count = 1
@csv_to_square
def execution(a, b, c):
    global count
    print(f'{count}: {square_roots(a, b, c)}')
    count += 1


@square_to_json
@csv_to_square
def all_inclusive(a, b, c):
    total = {}
    total[f'{a}, {b}, {c}'] = square_roots(a, b, c)
    return total


while True:
    print('\n=================== Menu ===================')
    print('1. Найти корни квадратного уравнения')
    print('2. Генерация csv с тремя случайными числами')
    print('3. Найти корни квадратного уравнения из csv')
    print('4. Найти корни из csv и записать в json')
    print('0. Выйти')
    menu = int(input('Выберите пункт меню: '))
    if menu == 1:
        print('Квадратное уравнение вида: ax^2 + bx + c = 0')
        a, b, c = input('Введите коэффициенты уравнения (a b c) через пробел: ').split()
        a, b, c = int(a), int(b), int(c)
        print(square_roots(a, b, c))
    elif menu == 2:
        csv_generate()
    elif menu == 3:
        execution()
        count = 1
    elif menu == 4:
        all_inclusive()
        count = 1
    elif menu == 0:
        exit()
    else:
        print(f'\nНеверно введена команда')
