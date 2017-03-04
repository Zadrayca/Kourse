
# Echo client program
import socket

HOST = '127.0.0.1'        # The remote host
PORT = 50007              # The same port as used by the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))     # соеденится с сервером по данным адресу и порту
    s.sendall(b'Hello, world')  # модуль работает с байтами
    data = s.recv(1024)
print('Received', repr(data))
