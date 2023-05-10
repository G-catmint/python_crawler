# 01 拿到conID
# 02 拿到vidoStatus返回json内容 ->srcURL
# 03 拿到srcURL里面的内容进行修整
# 04 下载视频
import random
import time
from lxml import etree
import requests

url = "https://www.pearvideo.com/video_1455632"
contId = url.split("_")[1]

header = {
    "User-Agent": ":Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.58",
    f"Referer": f"{url}"
}

vidoStatus = f"https://www.pearvideo.com/videoStatus.jsp?contId={contId}&mrd=0.8449253822112737"

resp = requests.get(url=vidoStatus,headers=header)
resp_url = requests.get(url=url)
html = etree.HTML(resp_url.text)
name = html.xpath("/html/body/div[2]/div[1]/div[2]/div/div[1]/h1/text()")[0]

dic = resp.json()
systemTime = dic["systemTime"]
srcUrl = dic["videoInfo"]["videos"]["srcUrl"]
srcUrl = srcUrl.replace(systemTime,f"cont-{contId}")

# 下载视频
resp_src = requests.get(srcUrl)
home = "E:/python/python-learning/第二阶段爬虫学习/03 requests进阶概述/下载视频/" + f"{name}.mp4"
with open(home, mode="wb") as f:
    f.write(resp_src.content)

time.sleep(random.random()*20)
resp.close()
resp_src.close()