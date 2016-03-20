# Echo client program
import socket

nick = 'vensder'

HOST = '192.168.1.116'    # The remote host
PORT = 8888              # The same port as used by the server

# Создаем объект сокета(объект соединения)
# тип связи, тип соединения TCP/IP, потоковое.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# соединяемся по адресу и порту
s.connect((HOST, PORT))

def send_message(text):
	# шлем данные - набор байтов (массив)
	s.sendall(bytes(text, 'utf-8'))
	# получаем ответ от сервера
	# 1024 ограничение данных
	#data = s.recv(1024)
	#s.close()
	#print('Received', repr(data))

while True:
	text = input('>')
	if text == 'exit':
		s.close()
		quit()
	print(text)
	send_message(text)
	#s.close()

s.close()
