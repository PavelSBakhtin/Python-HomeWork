# Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины:
# имена str, ставка int, премия str с указанием процентов вида «10.25%».
# В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии.

def generate_dict(names, pays, percents):
    return {name: pay * (1 + float(percent.strip('%')) / 100) for name, pay, percent in zip(names, pays, percents)}

names = ['Иван', "Петр", "Михаил"]
pays = [10000, 15000, 20000]
percents = ['50.25%', "20%", "30.6%"]

grants_dict = generate_dict(names, pays, percents)
print(grants_dict)
