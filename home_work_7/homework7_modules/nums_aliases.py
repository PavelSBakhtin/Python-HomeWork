from random import randint, uniform, shuffle, sample
from itertools import cycle

# Функция, которая заполняет файл (добавляет в конец) случайными парами чисел.
# Первое число int, второе - float разделены вертикальной чертой.
# Минимальное число - -1000, максимальное - +1000.


def numbers(lines, file_name):
    with open(file_name, 'a', encoding='utf-8') as file:
        for _ in range(lines):
            file.write(f'{randint(-1000, 1000)}|{round(uniform(-1000, 1000), 3)}\n')


def input_mode():
    n = int(input('Select input mode number of lines - manual (1), random (2): '))
    if n == 1:
        numbers(int(input('Enter the number of lines: ')), 'homework7_nums.txt')
    elif n == 2:
        numbers(randint(1, 5), 'homework7_nums.txt')
    else:
        print('Wrong number')


# Функция, которая генерирует псевдоимена.
# Имена начинаются с заглавной буквы, состоять из 4-7 букв,
# среди которых обязательно присутствуют гласные.


name_list = []


def generate_aliases(lists):
    vowels = 'аеёиоуыэюя'
    consonants = 'бвгджзйклмнпрстфхцчшщъь'
    name_counts = int(input('Number of aliases to generate: '))
    for _ in range(0, name_counts):
        name_length = randint(4, 7)
        count_vowels = randint(1, name_length - 2)
        count_consonants = name_length - count_vowels
        name_vowels = sample(vowels, count_vowels)
        name_consonants = sample(consonants, count_consonants)
        aliase = name_vowels + name_consonants
        shuffle(aliase)
        final_aliase = ''.join(aliase).title()
        lists.append(final_aliase)
    return lists


def file_entry():
    data = generate_aliases(name_list)
    with open('homework7_aliases.txt', 'a', encoding='utf-8') as f:
        for line in data:
            print(line, end='\n', file=f)


# Функция, которая открывает на чтение созданные выше файлы с числами и именами.
# Перемножает пары чисел. В новый файл сохраняет имя и произведение:
# - если результат умножения отрицательный,
# сохраняются имя записанное строчными буквами и произведение по модулю;
# - если результат умножения положительный,
# сохраняются имя прописными буквами и произведение округлённое до целого.
# В результирующем файле столько же строк, сколько в более длинном файле.
# При достижении конца более короткого файла, возвращается его начало.


def write_file():
    f1_size = len(list(1 for _ in open('homework7_nums.txt')))
    f2_size = len(list(1 for _ in open('homework7_aliases.txt')))
    count = max(f1_size, f2_size)

    with open('homework7_nums.txt', 'r', encoding='utf-8') as f1, \
            open('homework7_aliases.txt', 'r', encoding='utf-8') as f2, \
            open('homework7_nums_aliases.txt', 'w', encoding='utf-8') as f3:
        f1_list = cycle(f1.readlines())
        f2_list = cycle(f2.readlines())
        for _ in range(count):
            f1_item_1, f1_item_2 = next(f1_list).split('|')
            f1_res = round(float(f1_item_1) * float(f1_item_2), 3)
            if f1_res < 0:
                print(f'{next(f2_list).strip().lower()}:{abs(f1_res)}', file=f3)
            else:
                print(f'{next(f2_list).strip().upper()}:{round(f1_res)}', file=f3)


if __name__ == '__main__':
    pass
