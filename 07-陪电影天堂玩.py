import requests,re
import time,random

url = "https://www.dytt89.com/"
header = {
    "user-agent": ":Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.48"
}
resp = requests.get(url=url)
resp.encoding = "gb2312"

obj1 = re.compile(r"2023必看热片.*?<ul>(?P<test>.*?)</ul>", re.S)
obj2 = re.compile(r"<a href='(?P<href>.*?)'",re.S)
obj3 = re.compile(r'◎片　　名(?P<movie>.*?)<br />.*?<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(?P<download>.*?)">',re.S)

obf1 = obj1.finditer(resp.text)
child_helf_list = []
for it in obf1:
    ul = it.group('test')
    obf2 = obj2.finditer(ul)
    for itt in obf2:
        child_helf = url+itt.group('href').strip('/')
        child_helf_list.append(child_helf)


for href in child_helf_list:
    child_resp = requests.get(href)
    child_resp.encoding = "gb2312"
    obf3 = obj3.search(child_resp.text)
    print(obf3.group('movie'))
    print(obf3.group('download'))

time.sleep(random.random()*20)
resp.close()