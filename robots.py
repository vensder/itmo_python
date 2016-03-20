'''Б. 4. Представим, что делаем игру роботами.
У робота есть:
- скорость бега
- сила удара + дальность удара
- уровень брони
Придумайте 3-5 типов роботов и разместите их на поле боя.'''


class Robot:
    def __init__(self, speed, strike_power, strike_distance, armour, x, y):
        self.speed = speed
        self.strike_power = strike_power
        self.stike_distance = strike_distance
        self.armour = armour
        self.x = x
        self.y = y


class R2D2(Robot):
    def __init__(self, x, y):
        super().__init__(self, 100, 100, 100, 100, x, y)

class Android(Robot):
    def __init__(self, x, y):
        super().__init__(self, 10, 10, 10, 10, x, y)


r2d2 = R2D2(0,0)
