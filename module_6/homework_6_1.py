class Animal:

    def __init__(self, name):
        self.alive = True
        self.fed = False
        self.name = name

    def eat(self, food):
        if food.edible is True:
            self.fed = True
            print(f'{self.name} слопал {food.name}')
        else:
            self.alive = False
            print(f'{self.name} отказался есть {food.name}')


class Plant:

    def __init__(self, name):
        self.name = name
        self.edible = False


class Mammal(Animal):
    pass


class Predator(Animal):
    pass


class Flower(Plant):
    pass


class Fruit(Plant):
    def __init__(self, name):
        self.name = name
        self.edible = True


a1 = Predator('Хищник')
a2 = Mammal('Млекопитающее')
p1 = Flower('Цветок')
p2 = Fruit('Фрукт')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
