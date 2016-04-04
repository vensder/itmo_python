#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  2016_python.py
#  
#  Student Dmitry Makarov <vensder@gmail.com>



# Вспомним формат json.

# 1. Дан словарь Python:

cities = {
    "Gotham": {
        "pos": [12.16, 30.14],
        "size": 12080040
    },
    "Smallville": {
        "pos": [32.02, 40.63],
        "size": 28003000
    }
}


# Написать функцию, которая без использования
# стандартного или стороннего модуля json
# запишет входной словарь такого формата
# в файл формата json в таком виде:

# cities.json
{
    "Gotham": {
        "pos": [12.16, 30.14],
        "size": 12080040
    },
    "Smallville": {
        "pos": [32.02, 40.63],
        "size": 28003000
    }
}


print(cities)

def format_to_json(cities):

	format_json = str(cities).replace('\'','"')

	format_json = format_json.replace('{', '{\n    ')

	format_json = format_json.replace('}}', '\n    }\n}')

	format_json = format_json.replace('}, "', '},\n    "')

	format_json = format_json.replace(', "',',\n    "')

	format_json = format_json.replace('"pos"','    "pos"')

	format_json = format_json.replace('"size"','    "size"')

	format_json = format_json.replace('},', '\n    },') 
	
	return format_json



my_cool_string = format_to_json(cities)

print(my_cool_string)

with open ('cities.json', 'w') as output_file:
	output_file.write(my_cool_string)
	



# 2. Создадим свою замену классам,
# использванным в этом словаре (словарь, строка, список, числа..).
#
# Тогда задание такого словаря будет выглядеть следующим
# образом:
#
# cities = Cities(
#     City(name="Gotham", pos=Point(12.16, 30.14), size=Size(12080040)),
#     City(name="Smallville", pos=Point(32.02, 40.63), size=Size(28003000)),
# )
#
# Напишите эти классы.
