import csv
import json
import random
import time

from lxml import etree
import requests
from concurrent.futures import ThreadPoolExecutor
from fake_useragent import UserAgent

def download_one_page(args):
    # page = eval(input("输入要爬取的页数"))
    url = "http://www.xinfadi.com.cn/getPriceData.html"
    data = {
        "limit": 20,
        "current": args
    }
    header = {
        "User-Agent": ":Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.58"
    }
    resp = requests.post(url=url, headers=header, data=data)
    info = resp.json()
    list_resp = info['list']
    list_vegetable = []
    for vegetable in list_resp:
        dict_vegetable = {}
        dict_vegetable['prodCat'] = vegetable['prodCat']
        dict_vegetable['prodName'] = vegetable['prodName']
        dict_vegetable['lowPrice'] = vegetable['lowPrice']
        dict_vegetable['highPrice'] = vegetable['highPrice']
        dict_vegetable['avgPrice'] = vegetable['avgPrice']
        dict_vegetable['specInfo'] = vegetable['specInfo']
        dict_vegetable['place'] = vegetable['place']
        list_vegetable.append(dict_vegetable)

    if args == 1:
        with open("./北京新发地蔬菜价格查询.csv",'w',encoding='utf-8-sig',newline='')as f:
            writer = csv.writer(f)
            writer.writerow([' \tprodCat',' \tprodName',' \tlowPrice',' \thighPrice',' \tavgPrice',' \tspecInfo',' \tplace'])
            for line in list_vegetable:
                writer.writerow([' \t'+line['prodCat'],' \t'+line['prodName'],' \t'+line['lowPrice'],' \t'+line['highPrice'],' \t'+line['avgPrice'],' \t'+line['specInfo'],' \t'+line['place']])
    else:
        with open("./北京新发地蔬菜价格查询.csv", 'a', encoding='utf-8-sig', newline='') as f:
            writer = csv.writer(f)
            for line in list_vegetable:
                writer.writerow([' \t' + line['prodCat'], ' \t' + line['prodName'], ' \t' + line['lowPrice'],
                                 ' \t' + line['highPrice'], ' \t' + line['avgPrice'], ' \t' + line['specInfo'],
                                 ' \t' + line['place']])
    print(f"第{args}页录入完成")

    time.sleep(random.random()*20)
    resp.close()


if __name__ == '__main__':
    with ThreadPoolExecutor(50) as t:
        for i in range(1,200):
            t.submit(download_one_page, i)
