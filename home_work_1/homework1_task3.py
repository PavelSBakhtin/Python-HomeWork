# Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: «Число является простым, если делится нацело только на единицу
# и на себя». Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

def simple(num: int) -> str:
    if num < 0 or num > 100000:
        return 'Input error, enter the valid number'
    else:
        count = 0
        for i in range(1, num + 1):
            if num % i == 0:
                count += 1
        if count <= 2:
            return "This number is simple"
        else:
            return "This number is not simple"

num = int(input('Enter the valid number: '))
print(simple(num))
