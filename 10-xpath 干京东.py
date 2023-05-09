import random
import time
from lxml import etree
import requests

url = "https://search.jd.com/Search?keyword=%E5%AE%8F%E5%9F%BA&enc=utf-8&suggest=1.def.0.base&wq=hongji&pvid=867bf42ee70e47aa8ff6f7c16f7b1ac0"

hread = {
    "user-agent": ":Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.58"
}

resp = requests.get(url=url,headers=hread)
# 解析
html = etree.HTML(resp.text)
i = 0
# 拿到所有电商的li
lis = html.xpath("/html/body/div[5]/div[3]/div[2]/div[1]/div/div[2]/ul/li")
for li in lis:
    i +=1
    price = li.xpath(f"./div/div[2]/strong/i/text()")[0].strip()
    name = li.xpath("./div/div[3]/a/em/text()")[0].strip()
    # comment = li.xpath("./div/div[4]/strong/text()")
    shopping = li.xpath("./div/div[5]/span/a/@title")[0]
    assessment = "".join(li.xpath("./div/div[6]/i/@data-tips"))
    country = li.xpath("./div/div[8]/@data-province")[0]

    print(price,name,shopping,assessment,country)


time.sleep(random.random()*20)
resp.close()