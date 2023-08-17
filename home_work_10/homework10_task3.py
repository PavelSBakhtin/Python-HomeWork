# Возьмите 1-3 любые задачи из прошлых семинаров (например сериализация данных), которые вы уже решали.
# Превратите функции в методы класса, а параметры в свойства.
# Задачи должны решаться через вызов методов экземпляра.

from random import shuffle


# Задача про банкомат:

class Atm:

    def __init__(self):
        self.balance = 0  # баланс
        self.count = 0  # счётчик пополнени/снияти
        self.operations = []  # список операций
        self._ACTION = 50  # кратность
        self._COMMISSION = 0.015  # % за снятие
        self._MIN_FEE = 30  # минимум такса при снятии
        self._MAX_FEE = 600  # максимум такса при снятии
        self._BONUS = 1.03  # % на остаток
        self._LIMIT = 5000000  # порог богатства
        self._TAX = 0.10  # налог на богатство

    def deposit_operations(self, operation):
        return self.operations.append(f'{self.count} >>> {operation}')

    def bonus(self):
        if self.count % 3 == 0 and self.count != int(self.operations[len(self.operations)-2][:len(str(self.count))]):
            self.balance *= self._BONUS
            print('\nВам начислено 3% на остаток')
        self.balance = round(self.balance, 2)
        return self.balance, self.count, self.operations

    def deposit_increase(self):
        print('\nПополнение баланса >>>')
        depo_plus = int(input('Введите сумму пополнения: '))
        if depo_plus % self._ACTION == 0:
            self.count += 1
            self.balance += depo_plus
            print(f'\nБаланс пополнен на сумму: {depo_plus}')
        else:
            print('\nПополнение невозможно, только кратно 50 у.е.')
        Atm.deposit_operations(self, f'Пополнение: {depo_plus}')
        self.balance, self.count, self.operations = Atm.bonus(self)
        print(f'\nБаланс: {self.balance} у.е.')
        return self.balance, self.count, self.operations

    def deposit_reduction(self):
        print('\nСниятие с баланса >>>')
        depo_minus = int(input('Введите сумму снятия: '))
        if depo_minus % self._ACTION == 0:
            fee = round(depo_minus * self._COMMISSION, 2)
            if fee < self._MIN_FEE:
                fee = self._MIN_FEE
            elif fee > self._MAX_FEE:
                fee = self._MAX_FEE
            total = depo_minus + fee
            if total < self.balance:
                self.count += 1
                self.balance -= total
                print(f'\nБаланс уменьшен на сумму: {total}')
            else:
                print('\nНедостаточно средств')
        else:
            print('\nСнятие невозможно, только кратно 50 у.е.')
        Atm.deposit_operations(self, f'Сниятие: {depo_minus}')
        self.balance, self.count, self.operations = Atm.bonus(self)
        print(f'\nБаланс: {self.balance} у.е.')
        return self.balance, self.count, self.operations


# Задача про ферзей:

class Chess:

    def __init__(self):
        self._N = 8
    
    def check_positions_ent(self, positions):
        for i in range(self._N):
            for j in range(i + 1, self._N):
                a, b = positions[i]
                c, d = positions[j]
                if a == c or b == d or abs(a - c) == abs(b - d):
                    return False
        return True

    def check_positions_rnd(self, positions):
        for i in range(self._N):
            for j in range(i + 1, self._N):
                if (positions[i] == positions[j] or
                    positions[i] - i == positions[j] - j or
                    positions[i] + i == positions[j] + j):
                    return False
        return True

    def main_ent(self):
        positions = []
        for i in range(1, 9):
            x, y = map(int, input(f'Введите координаты {i}-го ферзя через пробел: ').split())
            positions.append((x, y))
        print(f'\n{Chess.check_positions_ent(self, positions)}')

    def main_rnd(self, n):
        pos_line = list(range(1, 9))
        for _ in range(n):
            positions = []
            shuffle(pos_line)
            while not Chess.check_positions_rnd(self, pos_line):
                shuffle(pos_line)
            for i in range(1, 9):
                positions.append((i, pos_line[i - 1]))
            print(*positions)


# Основное выполнение программы:

def atm_task():
    atm = Atm()
    balance = atm.balance
    count = atm.count
    operations = atm.operations
    while True:
        print('\n========== БАНКОМАТ ==========')
        if balance > atm._LIMIT:
            balance -= (balance * atm._TAX)
        print(f'Баланс: {balance} у.е.')
        print('1. ПОПОЛНИТЬ')
        print('2. СНЯТЬ')
        print('3. СПИСОК ОПЕРАЦИЙ')
        print('0. ВЫЙТИ')
        menu = int(input('Выберите пункт меню: '))
        if menu == 1:
            balance, count, operations = atm.deposit_increase()
        elif menu == 2:
            balance, count, operations = atm.deposit_reduction()
        elif menu == 3:
            print('\nСписок операций:')
            print(*operations, sep='\n')
        elif menu == 0:
            print(f'\nБаланс: {balance} у.е.')
            exit()
        else:
            print(f'\nБаланс: {balance} у.е.')
            print(f'\nНеверно введена команда')


def queen():
    qu = Chess()
    print('= Расстановка ферзей =')
    print('1. Задать позиции')
    print('2. Рандомные позиции')
    menu = int(input('Выберите режим: '))
    if menu == 1:
        qu.main_ent()
    elif menu == 2:
        qu.main_rnd(n := int(input('Введите количество расстановок: ')))
    else:
        print('Неверно введена команда')


def tasks():
    print('1. Банкомат')
    print('2. Ферзи')
    menu = int(input('Выберите задачу: '))
    if menu == 1:
        atm_task()
    elif menu == 2:
        queen()
    else:
        print('Неверно введена команда')


tasks()
