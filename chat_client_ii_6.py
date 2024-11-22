import asyncio
import aioconsole


async def receive_responses(reader):
    while True:
        data = await reader.read(1024)
        if data == b'':
            print("Annonce : Le serveur est déconnecté")
            return

        print(">> ",data.decode())


async def send_data(writer):
    while True:
        message = await aioconsole.ainput(">> ")
        msg = message.encode()
        writer.write(msg)
        await writer.drain()


async def main():
    reader, writer = await asyncio.open_connection(host="10.6.6.20", port=8888)

    pseudo = "Hello|" + input("Entrez pseudo : ")
    pseudo_encoded = pseudo.encode()
    writer.write(pseudo_encoded)
    await writer.drain()

    tasks = [receive_responses(reader), send_data(writer)]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())