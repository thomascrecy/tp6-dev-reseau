import sys
import aiohttp
import aiofiles
import asyncio

file_path = "/tmp/web_page"

async def get_content(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            resp = await resp.read()
            return resp

async def write_content(content, file):
    async with aiofiles.open(file, mode="w", encoding="utf-8") as out:
        await out.write(content.decode())
        await out.flush() 

async def main():
    if len(sys.argv) != 2:
        print("Usage: python web_sync.py <URL>")
    else:
        url_request = sys.argv[1]
        html_content = await get_content(url_request)
        await write_content(html_content, file_path)
        print(f"Le contenu de la page a été téléchargé dans {file_path}.")

if __name__ == "__main__":
    asyncio.run(main())