# Echo server program
from json import loads
import socket


HOST = ''
PORT = 50007
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    while True:
        conn, addr = s.accept()
        with conn:
            # print('Connected by', addr)
            # data = conn.recv(1024)
            message = b''
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                message += data
            # получим словарь
            message = loads(message.decode('utf-8'))
            login = message.get('login')
            message = message.get('message')
            # print('login: {}'.format(login.decode('utf-8')))
            # print('message: {}'.format(message.decode('utf-8')))
            print('@{login}: {message}'.format(
                login = login,
                message = message
            ))