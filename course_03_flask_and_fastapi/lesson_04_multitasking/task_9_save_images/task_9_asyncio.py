from task_9_common import url_to_filename, parse
import asyncio
import aiohttp
import aiofiles
import time

async def download(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            filename = 'asyncio_' + url_to_filename(url)
            f = await aiofiles.open(filename, mode='wb')
            await f.write(await response.read())
            await f.close()
            print(f"Downloaded {url} in {time.time() - start_time:.2f} seconds")

async def main():
    tasks = []
    for url in urls:
        task = asyncio.create_task(download(url))
        tasks.append(task)
    await asyncio.gather(*tasks)

start_time = time.time()
if __name__ == '__main__':
    urls = parse()

    asyncio.run(main())