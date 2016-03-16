#my_circle_class.py

class Circle:
	

	def __init__(self, x, y, r):
		self.x = x 
		self.y = y
		self.r = r

	def area(self):
		return 3.14 * self.get_radius() * self.get_radius()

	@property
	def r(self):
		return self._r
	
	@r.setter
	def r(self, radius):
		if r < 0:
			raise ValueError('Radius should be positive')
		self._r = r

circle = Circle(0, 0, 1)

print(circle.area())

circle.set_radius(3)
print(circle.area())

circle.r = -10
print(circle.r)


