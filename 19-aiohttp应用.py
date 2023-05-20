import time

import aiohttp
import asyncio

urls = [
    "http://kr.shanghai-jiuxin.com/file/bizhi/20220927/ggbukl4pfgs.jpg",
    "http://kr.shanghai-jiuxin.com/file/bizhi/20220927/drq4w2w2cnd.jpg",
    "http://kr.shanghai-jiuxin.com/file/bizhi/20220927/betn5fg1g1s.jpg"
]

async def aiodownload(url):
    name = url.split('/')[-1]

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            with open(f"./19-图片/{name}","wb") as f:
                f.write(await resp.content.read())




async def main():
    tasks = []
    for url in urls:
        tasks.append(asyncio.create_task(aiodownload(url)))
    await asyncio.wait(tasks)


if __name__ == '__main__':
    t1 = time.time()
    asyncio.run(main())
    t2 = time.time()
    print(t2-t1)