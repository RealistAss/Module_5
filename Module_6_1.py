class Animal:
    alive = True
    fed =  False
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        if isinstance(food, Plant):
            if food.edible == True:

                self.fed = True
                print(f'{self.name} съел {food.name}')
            else:
                self.alive = False
                print(f"{self.name} не стал есть {food.name}")




class Plant:
    edible = False
    def __init__(self, name):
        self.name = name

class Mammal(Animal):
    pass


class Predator(Animal):
    pass


class Fruit(Plant):
    edible = True


class Flower(Plant):
    pass


a1 = Predator('Лев')

print(a1.eat('Мясо'))

a2 =Fruit('апельсин')

print(a1.eat(a2))

print(a1.fed)

f = Flower('Одвуанчик')

a1.eat(f)