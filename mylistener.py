import socket, train_monitor
BUFSIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(("0.0.0.0", 8890))
sock.listen(5)

while True:
    try:
        client, cltadd = sock.accept()
        print('Receive data from {}.'.format(cltadd))
        data = client.recv(BUFSIZE)
        data = data.decode('utf8').split(' ')
        train_monitor.train_monitor(data[0],data[1],data[2],data[3])
        client.sendall(b'Monitor Start')
        print('Monitor Start')
    except socket.error:
        continue
