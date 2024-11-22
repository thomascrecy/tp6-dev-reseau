import asyncio

global CLIENTS
CLIENTS = {}

async def handle_client_msg(reader, writer):
    while True:
        data = await reader.read(1024)
        addr = writer.get_extra_info('peername')

        if data == b'':
            break

        CLIENTS[addr] = {}
        CLIENTS[addr]["r"] = reader
        CLIENTS[addr]["w"] = writer

        message = data.decode()
        print(f"Message received from {addr[0]}:{addr[1]} : {message!r}")

        for (c_addr, c_data) in CLIENTS.items():
            if c_addr != addr:
                c_data["w"].write(f"{addr[0]}:{addr[1]} a dit : {message}".encode())
        await writer.drain()


async def main():
    server = await asyncio.start_server(handle_client_msg, '10.6.6.20', 8888)

    addrs = ', '.join(str(sock.getsockname()) for sock in server.sockets)
    print(f'Adresse du serveur : {addrs}')

    async with server:
        await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())