# Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

def file_info(strg) -> tuple:
    *way, file = strg.split("\\")
    full_way = "\\".join(way) + "\\"
    name, exten = file.split(".")
    return full_way, name, exten

adress = 'D:\учёба\Python\Python.jpg'
print(file_info(adress))
