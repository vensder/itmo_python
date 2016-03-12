
class Dog:
	usy = True

class Utka:
	krylya = True
	
class Gus:
	kluv = True
	
class Lebed(Utka, Gus): # наследован
	pass

leb = Lebed()

print(leb.kluv, leb.krylya)

print(type(leb))
print(isinstance(leb, Lebed))
print(isinstance(leb, Utka))
print(isinstance(leb, Gus))
print(isinstance(leb, Dog))
