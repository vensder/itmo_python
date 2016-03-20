# Echo client program
import socket

HOST = 'localhost'    # The remote host
PORT = 50007              # The same port as used by the server


# Создаем объект сокета(объект соединения)
# тип связи, тип соединения TCP/IP, потоковое.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# соединяемся по адресу и порту
s.connect((HOST, PORT))

# шлем данные - набор байтов (массив)
s.sendall(b'Hello, world')

# получаем ответ от сервера
# 1024 ограничение данных
data = s.recv(1024)
s.close()

print('Received', repr(data))
