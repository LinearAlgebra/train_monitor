import socket
BUFSIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(("0.0.0.0", 8890))
sock.listen(5)

while True:
    client, cltadd = sock.accept()
    print('Receive data from {}.'.format(cltadd))
    data = client.recv(BUFSIZE)
    client.sendall(b'Data received')
    print(data.decode('utf8'))
