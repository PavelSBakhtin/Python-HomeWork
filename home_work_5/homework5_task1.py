# Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

import os

# Если надо расширение с точкой:
def file_info(strg) -> tuple:
    full_way, exten = os.path.splitext(strg)
    way, name = os.path.split(full_way)
    return way, name, exten

adress = 'D:\учёба\Python\Python.jpg'
print(file_info(adress))

# # Второе решение, с библиотекой os,
# # расширение без точки:
# def file_info(strg) -> tuple:
#     way = os.path.dirname(adress)
#     file = os.path.basename(adress)
#     name, exten = file.split(".")
#     return way, name, exten

# adress = 'D:\учёба\Python\Python.jpg'
# print(file_info(adress))

# # Первое решение, без библиотеки os:
# def file_info(strg) -> tuple:
#     *way, file = strg.split("\\")
#     full_way = "\\".join(way) + "\\"
#     name, exten = file.split(".")
#     return full_way, name, exten

# # Для себя:
# #
# # def file_info(strg) -> tuple:
# #     return way, name, exten
# #
# # или
# #
# # def file_info(strg):
# #     return (way, name, exten)
# #
# # если преобразование в кортеж не указано в имени функции, то указываем это в return
