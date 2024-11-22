import asyncio

global CLIENTS
CLIENTS = {}

async def handle_client_msg(reader, writer):
    while True:
        data = await reader.read(1024)
        addr = writer.get_extra_info('peername')

        if data == b'':
            break

        message = data.decode()
        print(f"Message received from {addr[0]}:{addr[1]} : {message!r}")

        if not addr in CLIENTS.keys():
            CLIENTS[addr] = {}
            CLIENTS[addr]["r"] = reader
            CLIENTS[addr]["w"] = writer

            if 'Hello|' in message:
                CLIENTS[addr]["pseudo"] = message.split("Hello|")[1]

                for client in CLIENTS.keys():
                    clientData = CLIENTS[client]

                    clientData["w"].write(f"Annonce : {CLIENTS[addr]["pseudo"]} a rejoint la chatroom".encode())

        else:
            for client in CLIENTS.keys():
                if client != addr:
                    clientData = CLIENTS[client]
                    clientData["w"].write(f"{CLIENTS[addr]["pseudo"]} a dit : {message}".encode())

        await writer.drain()


async def main():
    server = await asyncio.start_server(handle_client_msg, '10.6.6.20', 8888)

    addrs = ', '.join(str(sock.getsockname()) for sock in server.sockets)
    print(f'Adresse du serveur : {addrs}')

    async with server:
        await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())