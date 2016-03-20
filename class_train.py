

class Train:
	
	_objects_count = 0
	
	
	def __init__(self, cars = []):
		self._objects_count += 1
		
		self.cars = cars
		
	
	def __str__(self):
		return '{}: {}'.format(self.__class__.__name__, self.cars)

class Car:
	
	def __init__(self, weight):
		self.weight = weight
		

if __name__ == '__main__':
	
	train = Train()
	
	print(train)
	
	train2 = Train([Car(3), Car(5), Car(10)])
	
	print(train2
