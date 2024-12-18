import sys
import aiohttp
import aiofiles
import asyncio
import time

file_path = "/tmp/web_"

async def get_content(url):
    print(f"Téléchargement {url}")
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            resp = await resp.read()
            return resp

async def write_content(content, file):
    async with aiofiles.open(file, mode="w", encoding="utf-8") as out:
        await out.write(content.decode())
        await out.flush() 

async def process_url(url, dl_file):
    content = await get_content(url)
    await write_content(content, dl_file)

async def main():
    start_time = time.time()

    if len(sys.argv) != 2:
        print("Usage: python web_sync.py <URL>")
    else:
        urls_file = sys.argv[1]
        tasks = []
        with open(urls_file, "r", encoding="utf-8") as file:
            urls = file.readlines()
            for url in urls:
                url = url.split("\n")[0]
                url_formatted = url.split("://")[1]
                urlFile = file_path+url_formatted

                tasks.append(process_url(url, urlFile))
            await asyncio.gather(*tasks)
    
    end_time = time.time()
    print(f"Execution time: {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    asyncio.run(main())