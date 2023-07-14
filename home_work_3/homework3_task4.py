# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.
# * Верните все возможные варианты комплектации рюкзака.

import random

things = {}
things["нож"] = 1
things["спички"] = 1
things["топор"] = 2
things["котел"] = 2
things["аптечка"] = 3
things["вода"] = 4
things["палатка"] = 5

list = []
for i in things.keys():
    list.append(i)

def baggage(things, max_weight):
    possible = []
    a = random.randint(0, 6)
    possible.append(list[a])
    max_weight -= things.get(list[a])
    for thing, weight in things.items():
        if weight <= max_weight and thing not in possible:
            possible.append(thing)
            max_weight -= weight
    return possible

max_weight = 15
print(*baggage(things, max_weight)) 
