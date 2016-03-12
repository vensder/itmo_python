import random

class Transport:
	
	def __init__(self, name, speed = 0, wheel_count = 0, mass = 0, color = (0,0,0)):
		self.name = name
		self.speed = speed
		self.wheel_count = wheel_count
		self.mass = mass
		self.color = color
		self.pos = 0
		
	def drive(self, time):
		self.pos += self.speed * time
		#return self.pos
		
	def show_pos(self):
		print(self.name, ':', self.pos)
		
		
class Car(Transport):
	
	def __init__(self, name):
		super().__init__(name, speed = 120, wheel_count = 4, mass = 2, color = (0,255,0))
		
class Tank(Transport):
	
	def __init__(self, name):
		super().__init__(name, speed = 120, wheel_count = 4, mass = 2, color = (0,255,0))
		
		self.can_fire = True
		
class Airplane(Transport):
	
	def __init__(self, name):
		super().__init__(name, speed = 800, wheel_count = 22, mass = 100, 
			color = (250,250,250))
		
		self.wings_count = 2
		self.tail = True
		
machines = [
	Car('car-1'),
	Tank('tank-1'),
	Airplane('plane-1'),
	Car('car-2'),
	Tank('tank-2'),
	Airplane('plane-2'),

]

for m in machines:
	if hasattr(m, 'fire'):
		m.fire()
		
	
for m in machines:
	m.show_pos()

for m in machines:
	time = random.randint(1, 150)
	m.drive(10)

print('-'*20)

for m in machines:
	m.show_pos()
	
