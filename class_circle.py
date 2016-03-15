import math


class Circle:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
        
    def area(self):
        return math.pi * self.r ** 2
    
    @property    
    def r(self):
        return self._r
    
    @r.setter
    def r(self,r):
        if r < 0:
            raise ValueError('Radius should be nonnegative')
        self._r = r

c = Circle(0, 0, 1)
print(c.x)
print(c.y)

c.r = 2
print(c.r)
