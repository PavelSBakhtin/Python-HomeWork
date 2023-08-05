# Напишите функцию группового переименования файлов.
# Она должна:
# * принимать параметр - желаемое конечное имя файлов,
#   при переименовании в конце имени добавляется порядковый номер;
# * принимать параметр - количество цифр в порядковом номере;
# * принимать параметр - расширение исходного файла,
#   переименование должно работать только для этих файлов внутри каталога;
# * принимать параметр - расширение конечного файла;
# * принимать диапазон сохраняемого оригинального имени - например,
#   для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла,
#   к ним прибавляется желаемое конечное имя, если оно передано;
#   далее счётчик файлов и расширение.

import os


def group_rename(name_fin, length, ext_org, ext_fin, name_org, path='.'):
    count = 1
    for file in os.listdir(path):
        if file.endswith(ext_org):
            file_org = os.path.splitext(file)[0]
            temp = file_org[name_org[0]-1:name_org[1]] if name_org else ''
            file_fin = f'{temp}{name_fin}{str(count).zfill(length)}{ext_fin}'
            os.rename(os.path.join(path, file), os.path.join(path, file_fin))
            count += 1


group_rename('hoba', 4, '.txt', '.png', [1, 5], './homework7_task2')
