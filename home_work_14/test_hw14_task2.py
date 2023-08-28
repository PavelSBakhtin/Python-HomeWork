# Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях.
# Напишите к ним тесты, 2-5 тестов на задачу в трёх вариантах:
# doctest, unittest, pytest.

# Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: «Число является простым, если делится нацело только на единицу
# и на себя». Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

import doctest
import unittest
import pytest


def simple(num: int) -> str:
    """
    Число является простым или составным:
    >>> simple(13)
    True
    >>> simple(444)
    False
    >>> simple(-7)
    'Input error, enter the valid number'
    """
    if num < 0 or num > 100000:
        return 'Input error, enter the valid number'
    else:
        count = 0
        for i in range(1, num + 1):
            if num % i == 0:
                count += 1
        return count <= 2


class TestSimple(unittest.TestCase):

    def test_simple(self):
        self.assertTrue(simple(13), True)

    def test_simple(self):
        self.assertFalse(simple(444), False)

    def test_simple(self):
        self.assertNotIn(simple(-7), (lambda x: x for _ in range(1, 100001)))


@pytest.mark.parametrize('number, result', [(13, True), (444, False), (-7, 'Input error, enter the valid number')])
def test_simple(number, result):
    assert (simple(number) == result)


doctest.testmod(verbose=True)
unittest.main(verbosity=2)
pytest.main(['-v'])
