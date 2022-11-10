import socket

HOST = '127.0.0.1'
PORT = 55000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind((HOST, PORT))
    sock.listen()
    print('Word count setver is running. ctr+c if stop')
    while True:
        conn, addr = sock.accept()
        print('connected: ', addr)
        request = conn.recv(1024)
        sum = 0
        for i in str(request).split(' '):
            if i.isalpha() or len(i) > 1 :
                sum += 1
        reply = f'Number of words = {str(sum)}'
        conn.send(bytes(reply, encoding='UTF-8'))