import random
import time,re
from bs4 import BeautifulSoup
import requests

def download(href,i):
    ur = "https://www.umei.cc/"
    resp_pic = BeautifulSoup(href, "html.parser")
    pic_list = resp_pic.find("div", attrs={"class": "big-pic"})
    next_href = pic_list.find("a")
    next_href_name = ur + next_href.get("href")
    child_url = requests.get(next_href_name)
    child_url.encoding = "utf-8"

    img = pic_list.find("img")
    src = img.get("src")

    img_resp = requests.get(src)  # 用content拿到字节
    img_resp_name = "E:/python/python-learning/第二阶段爬虫学习/02 数据解析与提取/林心如人体艺术/" + src.split("/")[-1]

    with open(img_resp_name, mode="wb") as f:
        f.write(img_resp.content)  # 将字节写入文件 将文件名命名为.jpg

    print("over!")
    i-=1
    if i:
        pass
    else:
        exit()

    download(child_url.text,i)


ur = "https://www.umei.cc/"
url = "https://www.umei.cc/meinvtupian/xingganmeinv/"
resp = requests.get(url=url)
resp.encoding = "utf-8"

main_page = BeautifulSoup(resp.text, "html.parser")
main_list = main_page.find("div", attrs={"class": "item_list infinite_scroll"}).find_all("a")[6]
href = ur + main_list.get("href")

child_href = requests.get(url=href)
child_href.encoding = "utf-8"

i = 36

download(child_href.text,i)

time.sleep(random.random()*20)
resp.close()