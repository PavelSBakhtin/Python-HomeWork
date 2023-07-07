# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
# Программа должна подсказывать «больше» или «меньше» после каждой попытки.

import random

x = random.randint(1, 1001)
attempt = 10
print('Вы попали в игру - Угадай число!\nУ вас есть {} попыток'.format(attempt))
win = False

while attempt > 0:
    y = int(input('Введите число от 1 до 1000: '))
    if y > x:
        print('Загаданное число меньше')
        attempt -= 1
    elif y < x:
        print('Загаданное число больше')
        attempt -= 1
    else:
        print('Загаданное число угадано')
        win = True
        break
    print('Осталось попыток: ', attempt)

if win:
    print('Вы выйграли!\nНе использовано попыток: {}'.format(attempt - 1))
else:
    print('Вы проиграли...\nЗагаданное число: {}'.format(x))
