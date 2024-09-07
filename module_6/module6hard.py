class Figure:
    sides_count = 0
    def __init__(self, color, *sides):
        self.__color = list(color)
        self.filled = False
        if self.__is_valid_sides(*sides):
            self.__sides = list(sides)
        else:
            self.__sides = [1] * self.sides_count


    def get_color(self):  # возвращает цвет фигуры
        return self.__color

    def __is_valid_color(self, r, g, b):  # проверяет цвет на соответствие условиям
        return all(isinstance(value, int) and 0 <= value <= 255 for value in (r, g, b))

    def set_color(self, r, g, b):  # устанавливает цвет фигуры
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def set_sides(self, *sides):  # устанавливает стороны фигуры
        if self.__is_valid_sides(*sides):
            self.__sides = list(sides)
        # else:
        #     self.__sides = [1] * self.sides_count

    def __is_valid_sides(self, *sides):  # проверяет стороны на соответствие условиям
        return all(isinstance(value, int) and len(sides) == self.sides_count and value > 0 for value in sides)

    def get_sides(self):  # возвращает указанные длины сторон
        return (self.__sides)

    def __len__(self):
        return sum(self.__sides)

import math  # загружаем модуль для использования числа ПИ

class Circle(Figure):
    sides_count = 1
    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__radius = None

    def get_square(self):
        self.__radius = self.get_sides()[0] / (2 * math.pi)  # вычисляем рауиус окружности
        return self.__radius ** 2 * math.pi  # вычисляем площадь окружности

class Triangle(Figure):
    sides_count = 3
    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__height = None


    def calculate_height(self):  # вычисляем высоту треугольника
        a, b, c = self.get_sides()
        s = (a + b + c) / 2
        return (2 / a) * math.sqrt(s * (s - a) * (s - b) * (s - c))

    def get_square(self):  # вычисляем площадь треугольника
        a = self.get_sides()[0]
        return 0.5 * a * self.calculate_height()


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        if len(sides) == 1:
            sides = [sides[0]] * self.sides_count
        super().__init__(color, *sides)

    def get_volume(self):
        return self.get_sides()[0] ** 3  # вычисляем объем куба

    def set_sides(self, *sides):
        if len(sides) == 1:
            sides = [sides[0]] * self.sides_count
            super().set_sides(*sides)
    #     else:
    #         super().set_sides(*sides)



circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)

circle1.set_color(55, 66, 77)
print(circle1.get_color())
print(circle1.get_sides())
circle1.set_sides(20)
print(circle1.get_sides())

print(circle1.get_square())
print(len(circle1))


tri1 = Triangle((20, 30, 50), 4, 5, 6)

print(tri1.get_square())
tri1.set_sides(7, 8, 9)
print(tri1.get_square())
print(len(tri1))

cube1 = Cube((222, 35, 130), 6)
cube1.set_color(300, 70, 15)
print(cube1.get_color())
cube1.set_sides(7)
print(cube1.get_sides())
print(cube1.get_volume())
cube1.set_sides(5)
print(cube1.get_volume())
