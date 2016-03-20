# Echo server program
import socket
# HOST = '192.168.1.116'
# HOST = 'localhost'
HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 8888              # Arbitrary non-privileged port

# создаем сокет
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# привязываем сокет к адресу порту
s.bind((HOST, PORT))

# начинаем слушать адрес порт
# кол-во ожидающих соединений
s.listen(1)

while True:
	# получаем соединение
	conn, addr = s.accept()
	# отображаем соединение
	print('Connected by', addr)

	while True:
		# получаем данные от клиента
		data = conn.recv(1024)
		print(data.decode('utf-8'))
		if not data: break # выходим из цикла, когдаданные закончатся
		# посылаем тоже самое обратно
		#conn.sendall(data)
	''''
	while True:
		text = input('>')
		if text == 'exit':
			s.close()
			quit()
		print(text)
	#send_message(text)
'''
	# закрываем сокет
	conn.close()

s.close()
