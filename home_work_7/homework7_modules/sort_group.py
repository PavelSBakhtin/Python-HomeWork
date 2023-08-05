import os

# Функция для сортировки файлов в директории по расширениям.


def replace_file():
    for file in os.listdir():
        exception = file.split('.')[-1]
        if not os.path.exists(exception):
            os.mkdir(exception)
        os.replace(file, os.path.join(os.getcwd(), exception, file))


# Функция группового переименования файлов.


def group_rename(name_fin, length, ext_org, ext_fin, name_org, path='.'):
    count = 1
    for file in os.listdir(path):
        if file.endswith(ext_org):
            file_org = os.path.splitext(file)[0]
            temp = file_org[name_org[0]-1:name_org[1]] if name_org else ''
            file_fin = f'{temp}{name_fin}{str(count).zfill(length)}{ext_fin}'
            os.rename(os.path.join(path, file), os.path.join(path, file_fin))
            count += 1


if __name__ == '__main__':
    pass
