import asyncio

HOST = '127.0.0.1'
PORT = 5050


async def main():
    try:
        reader, writer = await asyncio.open_connection(HOST, PORT)
        while True:
            message = input('Enter operation in format "x math_oper y" (wehre math_oper = +, -, *, /): ')
            writer.write(message.encode('utf8'))
            await writer.drain()
            request = await reader.read(1024)
            request = request.decode('utf8').strip()
            sender_address, sender_port = writer.get_extra_info('peername')
            print(f'<{sender_address} on {sender_port}>: {request}')
    except ConnectionRefusedError:
        print(f'Failed to connect to {HOST}:{PORT}')
    except ConnectionResetError:
        print(f'Server is down')


if __name__ == '__main__':
    asyncio.run(main())
