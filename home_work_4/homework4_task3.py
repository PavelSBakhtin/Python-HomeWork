# Возьмите задачу о банкомате из семинара 2.
# Разбейте её на отдельные операции — функции.
# Дополнительно сохраняйте все операции поступления и снятия средств в список.

balance = 0  # баланс
count = 0  # счётчик пополнени/снияти
operations = []  # список операций
ACTION = 50  # кратность
COMMISSION = 0.015  # % за снятие
MIN_FEE = 30  # минимум такса при снятии
MAX_FEE = 600  # максимум такса при снятии
BONUS = 1.03  # % на остаток
LIMIT = 5000000  # порог богатства
TAX = 0.10  # налог на богатство

def deposit_operations(bill: list, count, operation):
    bill.append(f'{count} >>> {operation}')
    return bill

def deposit_increase(balance, count, operations):
    print('\nПополнение баланса >>>')
    depo_plus = int(input('Введите сумму пополнения: '))
    if depo_plus % ACTION == 0:
        count += 1
        balance += depo_plus
    else:
        print('\nПополнение невозможно, только кратно 50 у.е.')
    print(f'\nБаланс пополнен на сумму: {depo_plus}')
    deposit_operations(operations, count, f'Пополнение: {depo_plus}')
    if count % 3 == 0:
        balance *= BONUS
        round(balance, 2)
        print('\nВам начислено 3% на остаток')
    print(f'\nБаланс: {balance} у.е.')
    return balance, count, operations

def deposit_reduction(balance, count, operations):
    print('\nСниятие с баланса >>>')
    depo_minus = int(input('Введите сумму снятия: '))
    if depo_minus % ACTION == 0:
        fee = round(depo_minus * COMMISSION, 2)
        if fee < MIN_FEE:
            fee = MIN_FEE
        elif fee > MAX_FEE:
            fee = MAX_FEE
        total = depo_minus + fee
        if total < balance:
            count += 1
            balance -= total
        else:
            print('\nНедостаточно средств')
    else:
        print('\nСнятие невозможно, только кратно 50 у.е.')
    print(f'\nБаланс уменьшен на сумму: {total}')
    deposit_operations(operations, count, f'Сниятие: {depo_minus}')
    if count % 3 == 0:
        balance *= BONUS
        round(balance, 2)
        print('\nВам начислено 3% на остаток')
    print(f'\nБаланс: {balance} у.е.')
    return balance, count, operations

while True:
    print('\n========== БАНКОМАТ ==========')
    if balance > LIMIT:
        balance -= (balance * TAX)
    print(f'Баланс: {balance} у.е.')
    print('1. ПОПОЛНИТЬ')
    print('2. СНЯТЬ')
    print('3. СПИСОК ОПЕРАЦИЙ')
    print('4. ВЫЙТИ')
    menu = int(input('Выберите пункт меню: '))
    if menu == 1:
        balance, count, operations = deposit_increase(balance, count, operations)
    elif menu == 2:
        balance, count, operations = deposit_reduction(balance, count, operations)
    elif menu == 3:
        print('\nСписок операций:')
        print(*operations, sep='\n')
    elif menu == 4:
        print(f'\nБаланс: {balance} у.е.')
        exit()
    else:
        print(f'\nБаланс: {balance} у.е.')
        print(f'\nНеверно введена команда')
