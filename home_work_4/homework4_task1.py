# Напишите функцию для транспонирования матрицы.

from random import randint

def matrix_create():
    row = int(input('Enter number of rows: '))
    col = int(input('Enter number of columns: '))
    matrix = list([[randint(10, 99) for i in range(col)] for j in range(row)])
    print('\nМатрица исходная:', *matrix, sep='\n')
    return matrix

def matrix_trans(matrix):
    transpose = list(map(list, zip(*matrix)))
    print('\nМатрица транспонированная:', *transpose, sep='\n')
    # return transpose

matrix_trans(matrix_create())
