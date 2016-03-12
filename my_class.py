# -*- coding: utf-8 -*-


class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

# И тогда мы можем создавать множестов точек:

points = [Point(10,12), Point(30,12), Point(10,30)]
for p in points:
	print(p, p.x, p.y)


class Polygon:
	
	def __init__(self, *points):
		self.points = points
		
		
	def show_points(self):
		for p in self.points:
			print(p.x, p.y)
#И тогда мы можем создавать полигоны точек

polygon = Polygon(
	Point(10,12),
	Point(30,12),
	Point(10,30)
	)

polygon.show_points()
polygon.points[2].y = 300
polygon.show_points()

#for p in polygon.points:
#	print(p.x, p.y)

quit()




# Поле экземпляра:
class B:
	
	# здесь общие поля
	count_of_b = 0
	
	#Конструктор
	def __init__(self):
		# поля конкретного объекта
		self.x = 10
		self.text = 'Hello'
		
		#print(count_of_b)
		
		self.count_of_b += 1


b = B()
b = B()

print('count ', b.count_of_b)


print(b.x, b.text)

#print(B.x, B.text)

print('---------------------')

cars = ['porshe', 'lada', 'volvo']
def car_to_upper(car):
	return car.upper()

class Car:
	arg = 'porche'
	def upper(self):
		return self.arg.upper()

a1 = car_to_upper(cars[1])
a2 = Car().upper()
print(a1, a2)

class A:
	arg = 'Python'

a = A()
print(a.arg)
a.arg = 'Spam'
A.arg = 332
print(a.arg)
b = A()
print(b.arg)


class B:
	def debug(self): # metod # self - ссылка на экземпляр
		print('Hello world')
		return 'Hello world'
b = B()
b.debug()
	
a = A() # exemlar
print(a.arg)


b = A() # another exemplar

print(a) #object a
print(A)

a.arg = 1 #attribute
b.blabla = lambda x: x*x

print(a.arg)
print(b.blabla(8))
