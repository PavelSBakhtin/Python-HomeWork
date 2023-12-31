# Функция, которая получает на вход директорию и рекурсивно обходит её,
# и все вложенные директории. Результаты обхода сохранит в файлы json, csv и pickle.
# ○ Для дочерних объектов указывает родительскую директорию.
# ○ Для каждого объекта укажит файл это или директория.
# ○ Для файлов сохранит его размер в байтах,
#   а для директорий размер файлов в ней, с учётом всех вложенных файлов и директорий.

import os
import json
import csv
import pickle


def get_size(path):
    result = 0
    for path_directory, path_names, file_names in os.walk(path):
        for i in file_names:
            i_path = os.path.join(path_directory, i)
            result += os.path.getsize(i_path)
    return result


def directory_walker(dir_path, path_to): # /homework8_files
    if not os.path.exists(path_to):
        os.mkdir(path_to)
    results = []
    for root_dir, dirs, files in os.walk(dir_path):
        for item in files:
            s_address = os.path.join(root_dir, item)
            results.append({'root_directory': root_dir,
                            'status': 'file',
                            'name': item,
                            'size_bytes': os.path.getsize(s_address)})

        for item in dirs:
            f_address = os.path.join(root_dir, item)
            results.append({'root_directory': root_dir,
                            'status': 'folder',
                            'name': item,
                            'size_bytes': get_size(f_address)})

    with open('../homework8_report/homework8_total.json', 'w') as json_file:
        json.dump(results, json_file, indent=2)

    with open('../homework8_report/homework8_total.csv', 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=results[0].keys())
        writer.writeheader()
        writer.writerows(results)

    with open('../homework8_report/homework8_total.pickle', 'wb') as pickle_file:
        pickle.dump(results, pickle_file)


if __name__ == '__main__':
    pass
