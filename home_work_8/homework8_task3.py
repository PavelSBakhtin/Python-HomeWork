# Соберите, из созданных на уроке и в рамках домашнего задания функций,
# пакет для работы с файлами разных форматов.

from homework8_task3.homework8_modules import txt_to_json, json_to_csv, csv_to_json, level_json
from homework8_task3.homework8_modules import json_to_pickle, pickle_to_csv, csv_to_pickle
from homework8_task3.homework8_modules import directory_walker

# в терминале из папки: homework8_task3

while True:
    print('\n================== Menu ==================')
    print('1. Преобразование файлов по форматам')
    print('2. Количество папок и файлов, и их размеры')
    print('3. Выйти')
    menu = int(input('Выберите пункт меню: '))
    if menu == 1:
        print('\n========== числа и имена ==========')
        print('1. Создать пары чисел')
        print('2. Создать псевдоимена')
        print('3. Объединить числа с псевдоименами')
        m1 = int(input('\nВыберите подпункт меню: '))
        if m1 == 1:
            pass
        elif m1 == 2:
            pass
        elif m1 == 3:
            pass
        else:
            print(f'\nНеверно введена команда')
    elif menu == 2:
        print('\n============ работа с файлами ============')
        print('1. Создать файлы, с указанным расширением')
        print('2. Создать файлы с разными расширениями')
        print('3. Создать файлы в указанную папку')
        m2 = int(input('\nВыберите подпункт меню: '))
        if m2 == 1:
            pass
        elif m2 == 2:
            pass
        elif m2 == 3:
            pass
        else:
            print(f'\nНеверно введена команда')
    elif menu == 3:
        exit()
    else:
        print(f'\nНеверно введена команда')
