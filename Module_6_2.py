class Vehicle:
    __COLOR_VARIANTS = ['red', 'black', 'white', 'green']
    def __init__(self, owner, __model, __engine_power, __color):
        self.owner = owner
        self.__model = __model
        self.__engine_power = __engine_power
        self.__color = __color


    def get_model(self):
        return f'Модель: {self.__model}'

    def get_horsepower(self):
        return f'Мощность двигателя: {self.__engine_power}'

    def get_color(self):
        return f'Цвет: {self.__color}'

    def print_info(self):
        print(self.get_model(), self.get_horsepower(), self.get_color(), f'Владелец: {self.owner}')

    def set_color(self, new_color):
        self.new_color = new_color
        if self.__color.lower in (i.lower for i in self.__COLOR_VARIANTS):
            self.__color = self.new_color
        else:
            print(f'Нельзя сменить цвет на: {self.new_color}')

class Sedan(Vehicle):
    __PASSANGER_LIMIT = 5






a = Sedan('Ilya', 'Toyota Mark II', 160, 'purple')
a.print_info()

a.set_color('red')
