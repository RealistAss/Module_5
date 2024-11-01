class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
        self.new_floor = None


    def go_to(self, new_floor):
        self.new_floor = new_floor
        if 1 <= self.new_floor <= self.number_of_floors:
            for i in range(1, new_floor + 1):
                print(i)
        else:
            print('Такого этажа не существует')


    def __len__(self):
        return self.number_of_floors


    def __str__(self):
        return (f'Название: {self.name}, кол-во этажей: {self.number_of_floors}')


    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
            return self

    def __iadd(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
            return self

a = House('ЖК Эльбрус', 30)
b = House('Мегаполис парк', 9)

print(a == b)

a += 10

print(a)

print(a > b)

print(a >= b)

print(a < b)

print(a <= b)

print(a != b)