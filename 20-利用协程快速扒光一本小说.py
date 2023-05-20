# http://dushu.baidu.com/api/pc/getCatalog?data={"book_id":"4306063500"}
# http://dushu.baidu.com/api/pc/getChapterContent?data={"book_id":"4306063500","cid":"4306063500|1569782244","need_bookinfo":1}
import json
import random
import aiohttp
import asyncio
import requests
import aiofiles

header = {
    "Referer": "http://dushu.baidu.com/pc/detail?gid=4306063500",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.64"
}

async def aiodownload(did,cid,name):
    data = {
        "book_id":f"{did}",
        "cid":f"{did}|{cid}",
        "need_bookinfo":1
    }
    header = {
        "Referer": "http://dushu.baidu.com/pc/reader?gid=4306063500&cid=1569782244",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.64"
    }
    datas = json.dumps(data)
    durl = 'http://dushu.baidu.com/api/pc/getChapterContent?data='+datas
    async with aiohttp.ClientSession() as session:
        async with session.get(url=durl) as resp:
            dic = await resp.json()
            # body = dic['data']['novel']['content']
            # with open(f"./西游记/{name}","w") as f:
            #     f.write(async body)
            async with aiofiles.open(f"./20-西游记/{name}",mode="w",encoding="utf-8") as f:
                await f.write(dic['data']['novel']['content'])


async def main(url):
    resp = requests.get(url,headers=header)
    dic = resp.json()
    tasks = []
    for item in dic['data']['novel']['items']:
        title = item['title']
        cid = item['cid']
        tasks.append(asyncio.create_task(aiodownload(did,cid,title)))
    await asyncio.wait(tasks)
    await asyncio.sleep(random.random()*5)
    resp.close()




if __name__ == '__main__':
    did = '4306063500'
    url = 'http://dushu.baidu.com/api/pc/getCatalog?data={"book_id":"4306063500"}'
    asyncio.run(main(url))