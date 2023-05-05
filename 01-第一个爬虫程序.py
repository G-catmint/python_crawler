from urllib.request import urlopen
url = "http://www.baidu.com"
resp = urlopen(url)

with open("E:/python/python-learning/第二阶段爬虫学习/0-10/mybaidu.html", mode="w", encoding="utf-8") as f:
    f.write(resp.read().decode("utf-8"))

print("over")