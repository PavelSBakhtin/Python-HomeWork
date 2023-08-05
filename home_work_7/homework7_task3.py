# Соберите, из созданных на уроке и в рамках домашнего задания функций, пакет для работы с файлами.

from homework7_modules import input_mode, file_entry, write_file
from homework7_modules import create_file, make_file, create_to_path
from homework7_modules import replace_file, group_rename


def show_extentions():
    extentions_dict = {1: 'png', 2: 'jpg', 3: 'bmp', 4: 'mov', 5: 'avi', 6: 'mp3', 7: 'txt'}
    for i in extentions_dict:
        print(f'{i}. {extentions_dict.get(i)}')
    choose = int(input(f'Выберите номер расширения: '))
    result = extentions_dict.get(choose)
    return result


def data_extentions():
    quantity = int(input('Укажите количество расширений: '))
    dict_ext = {}
    count = 1
    while quantity > 0:
        print(f'\nДля {count}-го расширения:')
        dict_ext[show_extentions()] = None
        quantity -= 1
        count += 1
    for i in dict_ext:
        dict_ext[i] = int(
            input(f'Укажите количество файлов для расширения .{i}: '))
    return dict_ext


while True:
    print('\n============ Menu ============')
    print('1. Функции с числами и именами')
    print('2. Работа с файлами')
    print('3. Сортировка и группы файлов')
    print('4. Выйти')
    menu = int(input('Выберите пункт меню: '))
    if menu == 1:
        print('\n========== числа и имена ==========')
        print('1. Создать пары чисел')
        print('2. Создать псевдоимена')
        print('3. Объединить числа с псевдоименами')
        m1 = int(input('\nВыберите подпункт меню: '))
        if m1 == 1:
            input_mode()
        elif m1 == 2:
            file_entry()
        elif m1 == 3:
            write_file()
        else:
            print(f'\nНеверно введена команда')
    elif menu == 2:
        print('\n============ работа с файлами ============')
        print('1. Создать файлы, с указанным расширением')
        print('2. Создать файлы с разными расширениями')
        print('3. Создать файлы в указанную папку')
        m2 = int(input('\nВыберите подпункт меню: '))
        if m2 == 1:
            create_file(show_extentions())
        elif m2 == 2:
            make_file(**(data_extentions()))
        elif m2 == 3:
            path_data = input('Укажите папку для создания файлов: ')
            create_to_path(path_data, show_extentions())
        else:
            print(f'\nНеверно введена команда')
    elif menu == 3:
        print('\n=== сортировка и группы файлов ===')
        print('1. Сортировки файлов по расширению')
        print('2. Групповое переименование файлов')
        m3 = int(input('\nВыберите подпункт меню: '))
        if m3 == 1:
            replace_file()
        elif m3 == 2:
            final = input('Укажите конечное имя файлов: ')
            length = int(
                input('Укажите количество цифр в порядковом номере: '))
            print('Укажите исходное расширение:')
            ext_org = show_extentions()
            print('Укажите конечное расширение:')
            ext_fin = show_extentions()
            print('Укажите диапазон сохраняемого оригинального имени')
            inp_range = input('цифрами ОТ и ДО через пробел: ')
            con_range = inp_range.split(' ')
            diap = []
            for i in con_range:
                diap.append(int(i))
            group_rename(final, length, '.'+ext_org, '.'+ext_fin, diap, './homework7_files')
        else:
            print(f'\nНеверно введена команда')
    elif menu == 4:
        exit()
    else:
        print(f'\nНеверно введена команда')

