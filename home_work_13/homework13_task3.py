# Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях.
# Напишите к ним классы исключения с выводом подробной информации.
# Поднимайте исключения внутри основного кода.
# Например, нельзя создавать прямоугольник со сторонами отрицательной длины.


# Прямоугольники


class DataException(Exception):

    def __init__(self, message: str):
        self.message = message

    def __str__(self):
        return f'{self.message}'


class SideValueError(DataException):

    def __init__(self, value):
        super(SideValueError, self).__init__(f'Стороны прямоугольника должны больше ноля: {value}')


class SquareValueError(DataException):

    def __init__(self, x_a, x_b, y_a, y_b):
        super(SquareValueError, self).__init__('Для вычитания одного прямоугольника из другого,\n'
                                               f'стороны вычитаемого {y_a, y_b} должны быть меньше сторон прямоугольника, из которого вычитают {x_a, x_b}')


class Descriptor:

    def __init__(self, data=None):
        self.data = data

    def __set_name__(self, owner, name):
        self._name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self._name, None)

    def __set__(self, instance, value):
        if value < 1:
            raise SideValueError(value)
        setattr(instance, self._name, value)


class Square:

    a = Descriptor()
    b = Descriptor()

    def __init__(self, a, b):
        self.a = a
        if b is None:
            self.b = a
        else:
            self.b = b

    def __add__(self, other):
        if isinstance(other, Square):
            return Square(self.a + other.a, self.b + other.b)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Square):
            if other.a > self.a or other.b > self.b:
                raise SquareValueError(self.a, self.b, other.a, other.b)
            return Square(self.a - other.a, self.b - other.b)
        return NotImplemented

    def get_area(self):
        return self.a * self.b

    def get_perimetr(self):
        return 2 * (self.a + self.b)

    def __repr__(self):
        return f'Square({self.a}, {self.b})'


square_1 = Square(3, 4)
square_2 = Square(5, 6)

square_3 = square_1 + square_2
square_4 = square_1 - square_2

print(square_3.__repr__())
print(square_4.__repr__())
