lst = ['poned', 1, 17, 20, 'vtor', 4, 6, 'poned', 10, 3]
days = {}
last_day = None
for a in lst:
	if type(a) is str and a not in days:
		days[a] = []
		last_day = a
	if type(a) is int:
		days[last_day].append(a)
		
print(days)		
print(a)
