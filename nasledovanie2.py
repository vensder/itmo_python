
# Изменение поведения словаря

class Mydict(dict):
	
	def get(self, key, default = 0):
		return dict.get(self, key, default)
		
		
a = dict(a = 1, b = 2)
b = Mydict(a = 1, b = 2)


b['c'] = 4

print(b)

print(a.get('v'))
print(b.get('v'))
