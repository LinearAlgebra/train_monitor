import socket

HOST = '127.0.0.1'
PORT = 8890


s.connect((HOST,PORT))

s.sendall(b'66666666666')
data = s.recv(1024)
print(data.decode('utf8'))