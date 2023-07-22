# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.

def dict_create():
    def dict_trans(**arg):
        return {i if i.__hash__ is not None else str(i): j for j, i in arg.items()}
    dict_insert = {'12': (1, 10), '45': 889, 'rand': ['jpg', 'pdf'], '754': 'anything'}
    print('\nСловарь исходный:', dict_insert, sep='\n')
    print('\nСловарь транспонированный:', dict_trans(**dict_insert), sep='\n')

dict_create()
