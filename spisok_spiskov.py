
#[имя, фамилия, деньги, процент успеваемсти]


spisok = [
	['Bob', 'Marly', 40.55, 1],
	['Ivan', 'Ivanov', 50.55, 0.9],
	['Sidor', 'Sidorov', 44.44, -0.4]
]

for name, surname, money, percent in spisok:
	print('{:<10} | {:<10} | {:>5.2f} | {:>6.1%}'.format(name, surname, money, percent))
