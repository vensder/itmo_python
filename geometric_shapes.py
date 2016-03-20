'''
А. 1. Есть базовый класс Фигура.
Далее есть набор фигур:
- круг
- прямоугольник
- треугольник
2. У них есть:
- точки с координатами - x и y
- толщина линии
- цвет
Создаем классы этих фигур.
3. Создаем некоторый "неслучайный" набор этих фигур (экземпляры классов).
По координатам позиционируем их так, чтобы потом когда мы научимся работать
с картинками, получилось осмысленное изображение.
'''


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move_by(self, dx, dy):
        self.x += dx
        self.y += dy

    def __str__(self):
        return '({}, {})'.format(self.x, self.y)

class Figure:
    def __init__(self, width, color):
        self.width = width
        self.color = color


class Triangle(Figure):
    def __init__(self, p1, p2, p3, width, color):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        super().__init__(width, color)

    def __str__(self):
        return '{}, {}, {}, {}'.format(self.__class__.__name__, self.p1, self.p2, self.p3)

    def move_by(self, dx, dy):
        self.p1.move_by(dx, dy)
        self.p2.move_by(dx, dy)
        self.p3.move_by(dx, dy)


class Rect(Figure):
    pass


class Circle(Figure):
    pass


t = Triangle(Point(0, 0), Point(1, 1), Point(1, 0), 2, 'blue')
print(t)
t.move_by(3, 4)
print(t)