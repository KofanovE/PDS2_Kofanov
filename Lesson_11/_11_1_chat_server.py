import socket
import pandas as pd
import requests

HOST = '127.0.0.1'
PORT = 55000

interval_var = '5min'
symbol = 'ETH'
url = f'https://www.alphavantage.co/query?function=CRYPTO_INTRADAY&symbol={symbol}&market=USD&interval={interval_var}&apikey=demo&datatype=csv'

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind((HOST, PORT))
    sock.listen()
    print('Server of chat "telegram_killer" is running. ctr+c if stop')
    while True:
        conn, addr = sock.accept()
        print('connected: ', addr)
        request = conn.recv(1024)
        print(str(request))
        if request.isdigit():
            if int(request) == 1:
                df = pd.read_csv(url)
                price = df['close'][0]
                reply = f'Actual prise ETH is: {price}'
                conn.send(bytes(reply, encoding='UTF-8'))
            else:
                reply = f'Unknown digit..'
                conn.send(bytes(f'***If you want actual price ETH - press 1*** Bot:  {reply}', encoding='UTF-8'))
        else :
            reply = input('Input your reply: ')
            conn.send(bytes(f'***If you want actual price ETH - press 1*** Bot:  {reply}', encoding='UTF-8'))





