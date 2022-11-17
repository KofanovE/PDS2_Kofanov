import asyncio
from asyncio import StreamReader, StreamWriter

HOST = '127.0.0.1'
PORT = 5050


async def main(host: str, port: int):
    print(f'Listening to {HOST} on port: {PORT}')
    server = await asyncio.start_server(asyncio_server, host, port)
    await server.serve_forever()


async def asyncio_server(reader: StreamReader, writer: StreamWriter):
    while True:
        message = await reader.read(1024)
        if not message:
            break
        message = message.decode('utf8').strip()
        sender_address, sender_port = writer.get_extra_info('peername')
        print(f'<{sender_address} on {sender_port}>: {message}')
        try:
            digit_1, oper, digit_2 = message.split(" ")
            digit_1 = float(digit_1)
            digit_2 = float(digit_2)
            if not oper in ["+", "-", "*", "/"]:
                raise ValueError
        except ValueError:
            message = "Send message in right format!"
        else:
            message = math_operations(digit_1, oper, digit_2)
        writer.write(message.encode('utf8'))
        await writer.drain()
    writer.close()


def math_operations(digit_1, oper, digit_2 ):
    try:
        if oper == "+":
            return f"{digit_1} {oper} {digit_2} = {digit_1 + digit_2}"
        elif oper == "-":
            return f"{digit_1} {oper} {digit_2} = {digit_1 - digit_2}"
        elif oper == "*":
            return f"{digit_1} {oper} {digit_2} = {digit_1 * digit_2}"
        elif oper == "/":
            return f"{digit_1} {oper} {digit_2} = {digit_1 / digit_2}"
    except ZeroDivisionError:
        return "ZeroDivisionError"



if __name__ == '__main__':
    asyncio.run(main(HOST, PORT))
