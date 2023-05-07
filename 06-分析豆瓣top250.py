# 那页面源代码 requests
# 通过re获取页面有效信息 re
import requests
import re
import csv
from pymysql import Connection

conn = Connection(
    host="localhost",
    port=3306,
    user="root",
    password="lzJ110011?",
    autocommit=True
)
cursor = conn.cursor()
conn.select_db("py1test")
# cursor.execute("create table pachong(order_name varchar(50),order_year int,order_score float,order_valuation int)")

url = "https://movie.douban.com//top250"
header = {
    "User-Agent":":Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.48"
}
rest = requests.get(url,headers=header)
obj = re.compile(r'<li>.*?<span class="title">(?P<name>.*?)</span>'
                 r'.*?<br>\n(?P<year>.*?)&nbsp;.*?'
                 r'<span class="rating_num" property="v:average">(?P<score>.*?)</span>.*?<span>(?P<valuation>.*?)人评价', re.S)
reach_finditer = obj.finditer(rest.text)
# f = open("E:/python/python-learning/第二阶段爬虫学习/数据解析与提取/abc.csv",mode="w",encoding="utf8")
sql = "insert into pachong(order_name,order_year,order_score,order_valuation) values(%s,%s,%s,%s)"

datas = []

for it in reach_finditer:
    value = [
        it.group('name'),
        it.group('year'),
        it.group('score'),
        it.group('valuation')
    ]
    datas.append(value)
    print(datas)

res = cursor.executemany(sql, datas)
rest.close()
conn.close()