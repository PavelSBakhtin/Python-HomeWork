import json
import csv
import pickle
import os


# Функция, которая создаёт из текстового файла новый с данными в формате JSON.
# Имена с большой буквы. Каждую пару сохраняет с новой строки.


def txt_to_json(file_in, file_out):
    with open(file_in, 'r', encoding='utf-8') as f1, \
            open(file_out, 'w', encoding='utf-8') as f2:
        data = f1.readlines()
        dict_to_save = {}
        for line in data:
            key, value = line.strip().split(":")
            if key.title() in dict_to_save.keys():
                dict_to_save[key.title()].append(value)
            else:
                dict_to_save[key.title()] = [value]
        json.dump(dict_to_save, f2, ensure_ascii=False, indent=2)


file_in = 'homework8_files/homework8_original.txt'
file_out = 'homework8_files/homework8_original.json'
txt_to_json(file_in, file_out)


# Функция, которая сохраняет созданный файл с данными в формате JSON в формате CSV.


def json_to_csv():
    with open('homework8_files/homework8_original.json', 'r') as f1, \
            open('homework8_files/homework8_original.csv', 'w', newline='', encoding='utf-8') as f2:
        data = json.load(f1)
        columns = ['level', 'pers_id', 'name']
        csv_write = csv.writer(f2, delimiter=';')
        csv_write.writerow(columns)
        result = []
        for key, value in data.items():
            for i in value:
                result.append([key, i, data[key][i]])
        csv_write.writerows(result)


json_to_csv()


# Чтение csv файла без использования csv.DictReader.
# Дополнит id до 10 цифр незначащими нулями.
# В именах первую букву сделает прописной.
# Добавит поле хеш на основе имени и идентификатора.
# Получившиеся записи сохранит в json файл,
# где каждая строка csv файла представлена как отдельный json словарь.
# Имя исходного и конечного файлов передаются как аргументы функции.


def csv_to_json(file_org, file_fin):
    with open(file_org, 'r', newline='') as f1, \
            open(file_fin, 'w', encoding='utf-8') as f2:
        csv_file = csv.reader(f1, delimiter=';')
        next(csv_file)
        dict_to_save = {}
        for level, pers_id, name in csv_file:
            pers_id = pers_id.rjust(10, '0')
            name = name.title()
            hash_id = hash(name + pers_id)
            dict_to_save[hash_id] = {level: [pers_id, name]}
        json.dump(dict_to_save, f2, indent=2)


csv_to_json('homework8_files/homework8_original.csv', 'homework8_files/homework8_whash.json')


# Функция, которая в бесконечном цикле запрашивает имя,
# личный идентификатор и уровень доступа (от 1 до 7).
# После каждого ввода добавляет новую информацию в JSON файл.
# Пользователи группируются по уровню доступа.
# Идентификатор пользователя выступает ключём для имени.
# Все идентификаторы уникальны независимо от уровня доступа.
# При перезапуске функции уже записанные в файл данные сохраняться.


def level_json():
    while True:
        str_inp = input('Введите данные через пробел: ')
        if str_inp:
            name, pers_id, level = str_inp.split()
            if not 0 < int(level) < 8:
                print('Неверный уровень доступа')
                continue
            with open('homework8_files/homework8_level.json', 'r') as f1:
                try:
                    data = json.load(f1)
                except:
                    data = {}
            if level not in data:
                data[level] = {}
            data[level][pers_id] = name
            with open('homework8_files/homework8_level.json', 'w') as f2:
                json.dump(data, f2, sort_keys=True)
        else:
            break


level_json()


# Функция, которая ищет json файлы в указанной директории
# и сохраняет их содержимое в виде одноимённых pickle файлов.


def json_to_pickle(path):
    for file in os.listdir(path):
        if file.endswith('.json'):
            file_name, file_ext = file.rsplit('.')
            with open(file, 'r') as f1, \
                    open(f'{file_name}.pickle', 'wb') as f2:
                pickle.dump(json.load(f1), f2)


json_to_pickle('homework8_files')


# Функция, которая преобразует pickle файл, хранящий список словарей, в табличный csv файл.
# Для тестирования взят pickle версию файла с hash.
# Функция извлекает ключи словаря для заголовков столбца из переданного файла.


def pickle_to_csv(file):
    path = os.getcwd()
    with open(file, 'rb') as f1, \
            open(f'{file[:-7]}.csv', 'w', newline='') as f2:
        data = pickle.load(f1)
        head = data.keys()
        writer = csv.writer(f2, delimiter=';')
        writer.writerow(head)
        for key, value in data.items():
            a, b = tuple(*value.values())
            writer.writerow([*(value.keys()), a, b])


pickle_to_csv('homework8_files/homework8_whash.pickle')


# Читает csv файл с hash без использования csv.DictReader.
# Распечатывает его как pickle строку.


def csv_to_pickle(file):
    with open(file, 'r', newline='') as f:
        csv_file = csv.reader(f, delimiter=';')
        count = 0
        values = []
        for line in csv_file:
            if count == 0:
                graphs = line
                count += 1
            else:
                values.append(line)
        dict_to_print = {}
        item = 0
        for key in graphs:
            dict_to_print[key] = values[item]
            item += 1
    print(f'{dict_to_print}\n')
    result = pickle.dumps(dict_to_print, protocol=pickle.DEFAULT_PROTOCOL)
    print(f'{result = }')
    print(type(result))


csv_to_pickle('homework8_files/homework8_whash.csv')


if __name__ == '__main__':
    pass
