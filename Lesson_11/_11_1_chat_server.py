import socket

HOST = '127.0.0.1'
PORT = 55000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind((HOST, PORT))
    sock.listen()
    print('Server of chat "telegram_killer" is running. ctr+c if stop')
    while True:
        conn, addr = sock.accept()
        print('connected: ', addr)
        request = conn.recv(1024)
        print(str(request))
        reply = input('Input your reply: ')
        conn.send(bytes(reply, encoding='UTF-8'))





