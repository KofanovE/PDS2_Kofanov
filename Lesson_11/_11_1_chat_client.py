import socket

HOST = '127.0.0.1'
PORT = 55000

while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((HOST, PORT))
        request = input('Input your request: ')
        sock.send(bytes(request, encoding='UTF-8'))
        reply = sock.recv(1024)
        print(reply)



