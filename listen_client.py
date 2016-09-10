import socket, sys

if __name__ == '__main__':
    HOST = '52.23.150.84'
    # HOST = '127.0.0.1'
    PORT = 8890


    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((HOST,PORT))

    s.sendall(bytes('k4604 济南 412313393@qq.com 1000'.encode('utf8')))
    data = s.recv(1024)
    print(data.decode('utf8'))
