# Доработаем задачи 5-6. Создайте класс-фабрику.
# - Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
# - Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.


class Animals:
    def __init__(self, name, age=None, color=None, voice=None):
        self.name = name
        self.age = age
        self.color = color
        self.voice = voice

    def give_info(self):
        print(f'{self.name = }')
        print(f'{self.age = }')
        print(f'{self.color = }')
        print(f'{self.voice = }')


class Mammal(Animals):
    def __init__(self, name, age, color, voice, swim):
        super().__init__(name, age, color, voice)
        self.swim = swim

    def special(self):
        print(f'{self.swim = }')


class Animal(Animals):
    def __init__(self, name, age=None, color=None, voice=None, breed=None):
        super().__init__(name, age, color, voice)
        self.breed = breed

    def special(self):
        print(f'{self.breed = }')


class Bird(Animals):
    def __init__(self, name, age, color, voice, fly):
        super().__init__(name, age, color, voice)
        self.fly = fly

    def special(self):
        print(f'{self.fly = }')


class Fish(Animals):
    def __init__(self, name, age, color, voice, oxygen):
        super().__init__(name, age, color, voice)
        self.oxygen = oxygen

    def special(self):
        print(f'{self.oxygen = }')


class Fabrica:

    def what(self, type_animal, *args, **kwargs):
        view = [Mammal, Animal, Bird, Fish]
        if type_animal in view:
            if type_animal == Mammal:
                being = Mammal(*args, **kwargs)
            elif type_animal == Bird:
                being = Bird(*args, **kwargs)
            elif type_animal == Fish:
                being = Fish(*args, **kwargs)
            else:
                being = Animal(*args, **kwargs)
            return being
        else:
            return Animal('Mammoth', 10000)


def wonder():
    create = Fabrica()
    whale = create.what(Mammal, name='Bag', age=10, color='gray', voice='gaf-gaf', swim=True)
    penguin = create.what(Bird, name='Linda', age=10, color='blue', voice='kar-kar', fly=False)
    anabas = create.what(Fish, name='Gera', age=10, color='dark', voice='mu-mu', oxygen=True)
    unknown = create.what('Ancient', name='Kuzja', age=10, color='brown', voice='uuuUUU')

    print(whale.give_info(), whale.special(), '\n')
    print(penguin.give_info(), penguin.special(), '\n')
    print(anabas.give_info(), anabas.special(), '\n')
    print(unknown.give_info(), unknown.special(), '\n')

wonder()
