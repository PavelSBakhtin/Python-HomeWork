# Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях.
# Напишите к ним классы исключения с выводом подробной информации.
# Поднимайте исключения внутри основного кода.
# Например, нельзя создавать прямоугольник со сторонами отрицательной длины.


# Матрицы


class DataException(Exception):

    def __init__(self, message: str):
        self.message = message

    def __str__(self):
        return f'{self.message}'


class LinesMatrixError(DataException):

    def __init__(self, matrix):
        super(LinesMatrixError, self).__init__('Строки матрицы должны иметь одинаковую длину:\n'
                                               f'{matrix}')


class SizeMatrixError(DataException):

    def __init__(self, a_l, b_l, a_c, b_c):
        super(SizeMatrixError, self).__init__('Размеры матриц должны совпадать для сложения:\n'
                                              f'Первая матрица состоит из = {a_l} строк, {a_c} столбцов;\n'
                                              f'Вторая матрица состоит из = {b_l} строк, {b_c} столбцов.')


class MultiplicationError(DataException):

    def __init__(self, x, y):
        super(MultiplicationError, self).__init__(f'Кол-во столбцов одной матрицы - {x}\n'
                                                  f'должно быть равно кол-ву строк второй матрицы - {y}')


class Matrices:

    def __init__(self, matrix):
        if len(set(len(row) for row in matrix)) != 1:
            raise LinesMatrixError(matrix)
        self.matrix = matrix

    def __print_matrix__(self):
        result = '\n'.join(['\t'.join(map(str, row)) for row in self.matrix])
        return result

    def __matching__(self, other):
        return self.matrix == other.matrix

    def __addition__(self, other):
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            raise SizeMatrixError(len(self.matrix), len(other.matrix),
                                  len(self.matrix[0]), len(other.matrix[0]))
        result = [[self.matrix[i][j] + other.matrix[i][j]
                  for j in range(len(self.matrix[0]))]
                  for i in range(len(self.matrix))]
        return Matrices(result)

    def __multiplication__(self, other):
        if len(self.matrix[0]) != len(other.matrix):
            raise MultiplicationError(len(self.matrix[0]), len(other.matrix))
        result = [[sum(self.matrix[i][k] * other.matrix[k][j]
                  for k in range(len(self.matrix[0])))
                  for j in range(len(other.matrix[0]))]
                  for i in range(len(self.matrix))]
        return Matrices(result)


m1 = Matrices([[1, 3, 5], [7, 9, 1], [3, 5, 7]])
m2 = Matrices([[2, 4, 6], [8, 0, 2], [4, 6, 8]])
m3 = Matrices([[1, 3, 5], [7, 9, 1], [3, 5, 7]])
m4 = Matrices([[2, 4], [6, 8], [1, 3]])

print(f'\n{m1.__print_matrix__()}')
print(f'\n{m2.__print_matrix__()}')
print(f'\n{m1.__matching__(m2)}')
print(f'\n{m1.__matching__(m3)}')
print(f'\n{(m1.__addition__(m2)).__print_matrix__()}')
print(f'\n{(m1.__multiplication__(m2)).__print_matrix__()}')
print(f'\n{(m1.__addition__(m4)).__print_matrix__()}')
print(f'\n{(m4.__multiplication__(m1)).__print_matrix__()}')
