# Соберите, из созданных на уроке и в рамках домашнего задания функций, пакет для работы с файлами.

from homework7_modules import input_mode, file_entry, write_file


while True:
    print('\n============ Menu ============')
    print('1. Функции с числами и именами')
    print('2. С')
    print('3. С')
    print('4. Выйти')
    menu = int(input('Выберите пункт меню: '))
    if menu == 1:
        print('\n======= числа и имена =======')
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
        pass
    elif menu == 3:
        pass
    elif menu == 4:
        exit()
    else:
        print(f'\nНеверно введена команда')
