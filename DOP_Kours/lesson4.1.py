
# Echo server program
import socket

# 80 порт - для интернет страниц

# 127.0.0.1 - localhost - внутренний адрес
# 192.168.1.10 - адрес в локальной сети
#

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))  # зарегистрировать адрес на сервере
    s.listen(1)           # запуск ожидания входящих соединений
    while True:
        conn, addr = s.accept()  # получаем следующее входящее соединение
        with conn: # соединение будет автоматически закрыто
            print('Connected by', addr)
            while True:
                data = conn.recv(1024)  # чтение из открытого сокета
                if not data: # проверка на то, что клиент больше не шлет данные
                    break
                conn.sendall(data) # отправляет данные клиенту

