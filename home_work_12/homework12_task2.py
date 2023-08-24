# Создайте класс студента:
# - Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв;
# - Названия предметов должны загружаться из файла CSV при создании экземпляра;
# - Другие предметы в экземпляре недопустимы;
# - Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100);
# - Также экземпляр должен сообщать средний балл по тестам для каждого предмета
#   и по оценкам всех предметов вместе взятых.

import csv


class Descriptor:
    """Дескриптор для проверки ФИО"""

    def __init__(self, data=None):
        self.data = data

    def __set_name__(self, owner, name):
        self._name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self._name, None)

    def __set__(self, instance, value):
        if not value.istitle() or not value.isalpha():
            raise ValueError('ФИО должно содержать только буквы и начинаться с заглавной')
        setattr(instance, self._name, value)


class Student:

    surname = Descriptor()
    first_name = Descriptor()
    second_name = Descriptor()
    
    def __init__(self, surname, first_name, second_name, csv_file='homework12_task2.csv'):
        self.surname = surname
        self.first_name = first_name
        self.second_name = second_name
        
        """Загрузка предметов из CSV файла"""
        with open(csv_file, 'r', encoding='UTF-8') as file:
            reader = csv.reader(file, delimiter='\n')
            self.subjects = {row[0]: {'grade': [], 'test_score': []} for row in reader}

    def __str__(self):
        return f'Студент: ФИО = {self.surname} {self.first_name} {self.second_name}'

    def grade_add(self, subject, grade):
        if subject not in self.subjects:
            raise ValueError(f'Предмет {subject} не найден')
        if grade < 2 or grade > 5:
            raise ValueError('Оценка должна быть от 2 до 5')
        self.subjects[subject]['grade'].append(grade)

    def test_score_add(self, subject, score):
        if subject not in self.subjects:
            raise ValueError(f'Предмет {subject} не найден')
        if score < 0 or score > 100:
            raise ValueError('Результат теста должен быть от 0 до 100')
        self.subjects[subject]['test_score'].append(score)

    def grade_average(self):
        total_grade = [grade for subject in self.subjects.values() for grade in subject['grade']]
        return sum(total_grade) / len(total_grade) if total_grade else 0

    def test_score_average(self, subject):
        if subject not in self.subjects:
            raise ValueError(f'Предмет {subject} не найден')
        total_score = self.subjects[subject]['test_score']
        return sum(total_score) / len(total_score) if total_score else 0


surname = Student.surname(input('Введите фамилию: '))
first_name = Student.first_name(input('Введите имя: '))
second_name = Student.second_name(input('Введите отчество: '))
