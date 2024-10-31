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


a = House('ЖК Эльбрус', 30)
a.go_to(21)
