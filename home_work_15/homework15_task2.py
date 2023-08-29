# Возьмите любые 1-3 задания из прошлых домашних заданий.
# Добавьте к ним логирование ошибок и полезной информации.
# Также реализуйте возможность запуска из командной строки с передачей параметров.
# Данная промежуточная аттестация оценивается по системе "зачет" / "не зачет".
# "Зачет" ставится, если Слушатель успешно выполнил задание.
# "Незачет" ставится, если Слушатель не выполнил задание.
# Критерии оценивания: 1 - Слушатель написал корректный код для задачи,
# добавил к ним логирование ошибок и полезной информации.

import argparse
import logging


logging.basicConfig(level=logging.INFO, filename='home_work_15/homework15_task2.log',
                    filemode='a', format='%(levelname)s, %(asctime)s, %(message)s')
                    # encoding='UTF-8' - работает с python 3.9


class SquareEquation:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.x1 = None
        self.x2 = None
        self.discriminant = None
        self.text = ''

    def roots(self):
        self.x1 = None
        self.x2 = None

        if self.a == 0:
            if self.b == 0:
                if self.c == 0:
                    self.text = 'the equation has an infinite number of roots'
                else:
                    self.text = 'equation writing error'
            else:
                self.x1 = self.x2 = -self.c / self.b

        else:
            self.discriminant = self.b ** 2 - 4 * self.a * self.c
            if self.discriminant < 0:
                self.text = 'the equation has no real roots'
            elif self.discriminant == 0:
                self.x1 = self.x2 = -self.b / (2 * self.a)

            else:
                self.x1 = (-self.b + self.discriminant ** 0.5) / (2 * self.a)
                self.x2 = (-self.b - self.discriminant ** 0.5) / (2 * self.a)

        return self.text, self.x1, self.x2


def parse_data(string):

    logging.info(f'line entered: {string}')

    try:
        a, b, c = string.split(' ')
        a = float(a)
        b = float(b)
        c = float(c)
        logging.info(f'the parameters of the equation {a}, {b}, {c}')

    except:
        logging.error('incorrect data format')
        raise ValueError('data entered incorrectly')

    return a, b, c


if __name__ == '__main__':

    try:
        parser = argparse.ArgumentParser(description='quadratic equation ax^2+bx+c = 0')
        parser.add_argument('-arg', type=str, nargs=3,
                            help='Enter parameters а b с:', default=['2', '3', '1'])
        args = ' '.join(parser.parse_args().arg)
    except:
        logging.error('command line input error')

    a, b, c = parse_data(args)

    print('quadratic equation {}x^2 + {}x + {} = 0'.format(a, b, c))

    text, x1, x2 = SquareEquation(a, b, c).roots()
    logging.info(f'result: {text}, equation roots {x1}, {x2}')

    print(text)
    if x1 is None and x2 is None:
        pass
    elif x2 == None:
        print(f'x1 = {x1}')
    else:
        print(f'x1 = {x1}, x2 = {x2}')
