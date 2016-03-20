
class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

class Shape:
	def __init__(self, width, color):
		self.width = width
		self.color = color

class Triangle(Shape):
	def __init__(self, width, color, p1, p2, p3):
		super().__init__(width, color)
		self.p1 = p1
		self.p2 = p2
		self.p3 = p3
		
t1 = Triangle(1,'blue', Point(0,0), Point(1,1), Point(1,0))

print(t1.width, t1.color, t1.p1.x, t1.p1.y)

