import socket

name = input('What is you name?\n')

sock = socket.socket()
sock.connect(('127.0.0.1', 8080))

sock.send(name.encode("utf-8"))

data = sock.recv(1024)
sock.close()

print(data.decode("utf-8"))