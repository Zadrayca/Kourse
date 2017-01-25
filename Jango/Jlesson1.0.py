
import socket

sock = socket.socket()

sock.bind(('127.0.0.1', 8080))

sock.listen(10)

conn, addr = sock.accept()

print('connected: ', addr)

while True:
    data = conn.recv(1024)
    if not data:
        break
    conn.send('Hello '.encode("utf-8") + data)


conn.close()

