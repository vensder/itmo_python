
import json

lst = ['foo', {'bar': ('baz', None, 1.0, 2)}]
json.dump(lst, open('jsonfile.json', 'w'))

print(json.dumps(lst))

lst2 = json.load(open('jsonfile.json'))
print('lst2:', type(lst2), lst2)

# имя и пароль записываем в json
# получем json и проверяем, отвечаем True/False

def write_user():
	login = input('login:')
	password = input('password:')
	
	d = {
		login: password
	} 
	
	return json.dumps(d)

def check_user(json_string):
	right_users = {
		'Alex': '1234',
		'Mahsa': 'dfaasdfa',
	}
	
	d = json.loads(json_string)
	name = list(d.keys())[0]
	if name in right_user[name]:
		return True
		
	return False 

print(check_user(write_user()))

