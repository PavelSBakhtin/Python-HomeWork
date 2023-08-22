# Создайте класс Матрица. Добавьте методы для:
# - вывода на печать,
# - сравнения,
# - сложения,
# - умножения матриц.

class Matrices:

    def __init__(self, matrix):
        if len(set(len(row) for row in matrix)) != 1:
            raise ValueError('Строки матрицы должны иметь одинаковую длину')
        self.matrix = matrix

    def __print_matrix__(self):
        result = '\n'.join(['\t'.join(map(str, row)) for row in self.matrix])
        return result

    def __matching__(self, other):
        return self.matrix == other.matrix

    def __addition__(self, other):
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            raise ValueError('Размеры матриц должны совпадать для сложения')
        result = [[self.matrix[i][j] + other.matrix[i][j]
                  for j in range(len(self.matrix[0]))]
                  for i in range(len(self.matrix))]
        return Matrices(result)

    def __multiplication__(self, other):
        if len(self.matrix[0]) != len(other.matrix):
            raise ValueError(
                'Кол-во столбцов одной матрицы должно быть равно кол-ву строк второй матрицы')
        result = [[sum(self.matrix[i][k] * other.matrix[k][j]
                  for k in range(len(self.matrix[0])))
                  for j in range(len(other.matrix[0]))]
                  for i in range(len(self.matrix))]
        return Matrices(result)


m1 = Matrices([[1, 3, 5], [7, 9, 1], [3, 5, 7]])
m2 = Matrices([[2, 4, 6], [8, 0, 2], [4, 6, 8]])
m3 = Matrices([[1, 3, 5], [7, 9, 1], [3, 5, 7]])

print(f'\n{m1.__print_matrix__()}')
print(f'\n{m2.__print_matrix__()}')
print(f'\n{m1.__matching__(m2)}')
print(f'\n{m1.__matching__(m3)}')
print(f'\n{(m1.__addition__(m2)).__print_matrix__()}')
print(f'\n{(m1.__multiplication__(m2)).__print_matrix__()}')
