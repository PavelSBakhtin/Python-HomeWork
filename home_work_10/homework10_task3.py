# Возьмите 1-3 любые задачи из прошлых семинаров (например сериализация данных), которые вы уже решали.
# Превратите функции в методы класса, а параметры в свойства.
# Задачи должны решаться через вызов методов экземпляра.


# Задача о банкомате:

class Atm:

    def __init__(self):
        self.balance = 0  # баланс
        self.count = 0  # счётчик пополнени/снияти
        self.operations = []  # список операций
        self.ACTION = 50  # кратность
        self.COMMISSION = 0.015  # % за снятие
        self.MIN_FEE = 30  # минимум такса при снятии
        self.MAX_FEE = 600  # максимум такса при снятии
        self.BONUS = 1.03  # % на остаток
        self.LIMIT = 5000000  # порог богатства
        self.TAX = 0.10  # налог на богатство

    def deposit_operations(self, operation):
        return self.operations.append(f'{self.count} >>> {operation}')

    def bonus(self):
        if self.count % 3 == 0 and self.count != int(self.operations[len(self.operations)-2][:len(str(self.count))]):
            self.balance *= self.BONUS
            print('\nВам начислено 3% на остаток')
        self.balance = round(self.balance, 2)
        return self.balance, self.count, self.operations

    def deposit_increase(self):
        print('\nПополнение баланса >>>')
        depo_plus = int(input('Введите сумму пополнения: '))
        if depo_plus % self.ACTION == 0:
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
        if depo_minus % self.ACTION == 0:
            fee = round(depo_minus * self.COMMISSION, 2)
            if fee < self.MIN_FEE:
                fee = self.MIN_FEE
            elif fee > self.MAX_FEE:
                fee = self.MAX_FEE
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


atm = Atm()
balance = atm.balance
count = atm.count
operations = atm.operations

while True:
    print('\n========== БАНКОМАТ ==========')
    if balance > atm.LIMIT:
        balance -= (balance * atm.TAX)
    print(f'Баланс: {balance} у.е.')
    print('1. ПОПОЛНИТЬ')
    print('2. СНЯТЬ')
    print('3. СПИСОК ОПЕРАЦИЙ')
    print('4. ВЫЙТИ')
    menu = int(input('Выберите пункт меню: '))
    if menu == 1:
        balance, count, operations = atm.deposit_increase()
    elif menu == 2:
        balance, count, operations = atm.deposit_reduction()
    elif menu == 3:
        print('\nСписок операций:')
        print(*operations, sep='\n')
    elif menu == 4:
        print(f'\nБаланс: {balance} у.е.')
        exit()
    else:
        print(f'\nБаланс: {balance} у.е.')
        print(f'\nНеверно введена команда')
