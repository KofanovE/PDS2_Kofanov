import socket
import pandas as pd
import requests
import logging

logger = logging.getLogger("Information")
logger.setLevel(logging.INFO)
fh = logging.FileHandler("new_snake.log")
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
fh.setFormatter(formatter)
logger.addHandler(fh)

HOST = '127.0.0.1'
PORT = 55000

interval_var = '5min'
symbol = 'ETH'
url = f'https://www.lphavantage.co/query?function=CRYPTO_INTRADAY&symbol={symbol}&market=USD&interval={interval_var}&apikey=demo&datatype=csv'

n = 1

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind((HOST, PORT))
    sock.listen()
    print('Server of chat "telegram_killer" is running. ctr+c if stop')
    while True:
        conn, addr = sock.accept()

        logger.info(f"connected: {addr}")

        print('connected: ', addr)
        request = conn.recv(1024)
        print(str(request))
        if request.isdigit():
            if int(request) == 1:
                try:
                    df = pd.read_csv(url)
                    price = df['close'][0]
                except Exception:
                    logger.error(f"URLError")
                    reply = f'Crypto_server is unavailable. Try later again! '
                    conn.send(bytes(reply, encoding='UTF-8'))
                    continue
                else:
                    logger.info(f"Respond price ETH: {price}$")

                    reply = f'Actual prise ETH is: {price}'
                    conn.send(bytes(reply, encoding='UTF-8'))
            else:
                reply = f'Unknown digit..'
                conn.send(bytes(f'***If you want actual price ETH - press 1*** Bot:  {reply}', encoding='UTF-8'))
        else :
            logger.warning(f"Connect the operator...")

            reply = f'Connect the operator! Waiting time is {n} hours.'
            conn.send(bytes(f'***If you want actual price ETH - press 1*** Bot:  {reply}', encoding='UTF-8'))
            n += 1





