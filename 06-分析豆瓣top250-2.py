import requests
import re
import csv
import random,time

url = "https://movie.douban.com//top250"
header = {
    "User-Agent":":Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.48"
}
rest = requests.get(url,headers=header)
obj = re.compile(r'<li>.*?<span class="title">(?P<name>.*?)</span>'
                 r'.*?<br>\n(?P<year>.*?)&nbsp;.*?'
                 r'<span class="rating_num" property="v:average">(?P<score>.*?)</span>.*?<span>(?P<valuation>.*?)人评价', re.S)
reach_finditer = obj.finditer(rest.text)
f = open("abc.csv",mode="w",encoding="utf-8")
csvwriter = csv.writer(f)
for it in reach_finditer:
    dic = it.groupdict()
    dic['year'] = dic['year'].split()
    csvwriter.writerows(dic.values())

print("over!")
time.sleep(random.random()*10)
rest.close()
f.close()