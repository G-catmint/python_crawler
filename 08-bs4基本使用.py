import random
import time
import requests
from bs4 import BeautifulSoup
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
# 访问今日菜价网站 以get拿取数据
url = "http://zhongdapeng.com/shucaijiage/1296.html"
reg = requests.get(url)
# print(reg.text)
# 过滤出想要的内容
reg.encoding = 'utf8'
resp = BeautifulSoup(reg.text, "html.parser") # html_encode='utf-8'
# print(resp.prettify())
rpf = resp.find("table", attrs={"cellspacing": "0", "width": "436"})
# print(rpf.prettify())
rpfa = rpf.find_all("tr")[1:]
sql = "insert into bs4(order_num,order_name,order_money,order_numb,order_vname,order_price) value(%s,%s,%s,%s,%s,%s)"

neum_all_list = []
for neum in rpfa:
    neum_list = []
    tds = neum.find_all("td")
    neum_list.append(tds[0].text.strip())
    neum_list.append(tds[1].text.strip())
    neum_list.append(tds[2].text.strip())
    neum_list.append(tds[3].text.strip())
    neum_list.append(tds[4].text.strip())
    neum_list.append(tds[5].text.strip())
    neum_all_list.append(neum_list)

print(neum_all_list)
cursor.executemany(sql, neum_all_list)
time.sleep(random.random()*20)
conn.close()
reg.close()