class Animal:
    def __init__(self, name):
        self.name = name

    alive = True
    fed = False

    def eat(self, food):
        self.food = food

        if isinstance(food, Fruit):
            Plant.edible = True

        if isinstance(food, Flower):
            Plant.edible = False

        if Plant.edible == False:
            print(f'{self.name} не стал есть {food.name}')
            Animal.alive = False

        if Plant.edible == True:
            print(f'{self.name} сожрал {food.name}')
            Animal.fed = True


class Predator(Animal):
    pass


class Mammal(Animal):
    pass


class Plant:
    def __init__(self, name):
        self.name = name

    edible = True


class Fruit(Plant):
    edible = True


class Flower(Plant):
    pass


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик-Cемицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)
print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
