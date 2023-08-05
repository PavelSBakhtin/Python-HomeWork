from string import ascii_letters
from random import randint, sample
import os

# Функция, которая создаёт файлы с указанным расширением.


def randbytes_py38(min_bytes, max_bytes):
    ONE_BYTE = 128
    count = randint(min_bytes, max_bytes)
    res = bytes('', encoding='utf_8')
    for _ in range(count):
        bt = randint(0, ONE_BYTE)
        res += bytes(chr(bt), encoding='utf_8')
    return res


def create_file(extention, count=None, short=6, long=30, min_bytes=256, max_bytes=4096):
    if count == None:
        count = int(input('\nКоличество файлов для создания: '))
    names = set()
    item = 1
    while len(names) < count:
        name = f'{item}' + ''.join(sample(ascii_letters, randint(short, long)))
        names.add(name)
        item += 1
    for i in names:
        size = randbytes_py38(min_bytes, max_bytes)
        with open(f'{i}.{extention}', 'wb') as file:
            file.write(size)


# Функция, которая генерирует файлы с разными расширениями.
# Расширения и количество файлов функция принимает в качестве параметров.
# Количество переданных расширений может быть любым.
# Количество файлов для каждого расширения различно.
# Внутри используется вызов функции из предыдущей функции.


def make_file(**extentions):
    for extention, count in extentions.items():
        create_file(extention=extention, count=count)


# Генерация файлов в указанную директорию — отдельный параметр функции.
# Отсутствие/наличие директории не вызывает ошибок в работе функции.
# Существующие файлы не удаляться/изменяться в случае совпадения имён.


def create_to_path(path, extention):
    if not os.path.exists(path):
        os.mkdir(path)
    os.chdir(path)
    create_file(extention)


if __name__ == '__main__':
    pass
