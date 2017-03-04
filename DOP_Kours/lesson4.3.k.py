from json import dumps
import socket

HOST = '127.0.0.1'
PORT = 50007

login = input('Login:')

while True:
    message = input('new message:')
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        data = dumps({
            'login': login,
            'message': message
        })
        s.sendall(data.encode('utf-8'))