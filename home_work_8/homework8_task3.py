# Соберите, из созданных на уроке и в рамках домашнего задания функций,
# пакет для работы с файлами разных форматов.

import os
from homework8_modules import txt_to_json, json_to_csv, csv_to_json, level_json
from homework8_modules import json_to_pickle, pickle_to_csv, csv_to_pickle
from homework8_modules import directory_walker

# В терминале работаем из ./home_work_8/homework8_files

while True:
    print('\n================== Menu ==================')
    print('1. Преобразование файлов по форматам')
    print('2. Количество папок и файлов, и их размеры')
    print('0. Выйти')
    menu = int(input('Выберите пункт меню: '))
    if menu == 1:
        m = True
        while m == True:
            print('\n========= преобразование файлов =========')
            print('1. Создать json файл с id и level')
            print('2. Создать json файл из txt')
            print('3. Создать csv файл из json')
            print('4. Создать json файл с hash из csv')
            print('5. Создать pickle файлы из json')
            print('6. Создать csv файл из pickle')
            print('7. Распечатать pickle строку из csv файла')
            print('0. Вернуться в основное меню')
            m1 = int(input('\nВыберите подпункт меню: '))
            if m1 == 1:
                level_json('homework8_level.json')
            elif m1 == 2:
                file_in = 'homework8_original.txt'
                file_out = 'homework8_original.json'
                txt_to_json(file_in, file_out)
            elif m1 == 3:
                json_to_csv()
            elif m1 == 4:
                csv_to_json('homework8_level.csv',
                            'homework8_hash.json')
            elif m1 == 5:
                json_to_pickle('homework8_pickle')
            elif m1 == 6:
                pickle_to_csv('homework8_pickle/homework8_hash.pickle')
            elif m1 == 7:
                csv_to_pickle('homework8_hash.csv')
            elif m1 == 0:
                m = False
            else:
                print(f'\nНеверно введена команда')
    elif menu == 2:
        m = True
        while m == True:
            print('\n============ папки и файлы, их размеры ============')
            print('1. Создать файлы, с указанным расширением')
            print('0. Вернуться в основное меню')
            m2 = int(input('\nВыберите подпункт меню: '))
            if m2 == 1:
                path = '../../home_work_8/homework8_files'
                path_to = '../../home_work_8/homework8_report'
                directory_walker(path, path_to)
            elif m2 == 0:
                m = False
            else:
                print(f'\nНеверно введена команда')
    elif menu == 0:
        exit()
    else:
        print(f'\nНеверно введена команда')
