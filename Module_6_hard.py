import math
class Figure:
    def __init__(self):
        self._color = [255, 255, 255]

    def get_color(self):
        return self._color

    def set_color(self, r, g, b):
        if self._is_valid_color(r, g, b):
            self._color = [r, g, b]
        else:
            print('Некорректные значения цвета')

    def _is_valid_color(self,r, g, b):
        return all(0 <= value <= 255 for value in (r, g, b))

class Circle(Figure):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def get_radius(self):
        return self.radius

    def set_radius(self, radius):
        if radius > 0:
            self.radius = radius
        else:
            print('Радиус должен быть положительным числом')

    def get_area(self):
        return math.pi*(self.radius**2)

    def get_perimetr(self):
        return 2*math.pi*self.radius

class Triangle(Figure):
    def __init__(self, side1, side2, side3):
        super().__init__()
        self.set_sides(side1, side2, side3)

    def _is_valid_triangle(self, side1, side2, side3):
        return (side1 + side2 > side3) and (side1 + side3 > side2) and (side2 + side3 > side1)

    def get_sides(self):
        return self._sides

    def set_sides(self, side1, side2, side3):
        if self._is_valid_triangle(side1, side2, side3):
            self._sides = [side1, side2, side3]
        else:
            print('Некорректные длины сторон треугольника')

    def get_area(self):
        a, b, c = self._sides
        s = self.get_perimetr()/2
        return math.sqrt(s*(s-a)*(s-b)*(s-c))

    def get_perimetr(self):
        return sum(self._sides)

class Cube(Figure):
    def __init__(self, edge_length):
        super().__init__()
        self.set_edge_length(edge_length)

    def get_edge_length(self):
        return self.get_edge_length

    def set_edge_length(self, edge_length):
        if edge_length > 0:
            self._edge_length = edge_length
        else:
            print('Длинна ребра должна быть положительным числом')

    def get_volume(self):
        return self._edge_length**3

    def get_surface_area(self):
        return 6*(self._edge_length**2)


