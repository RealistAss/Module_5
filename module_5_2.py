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


a = House('ЖК Эльбрус', 30)

print(len(a))
print(str(a))