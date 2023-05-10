# 登录 -> 获取cookie
# 带着cookie 去请求url
import random
import time

# 将以上两个操作连起来
# 我们可以使用session进行请求 -> session你可以认为是一连串的请求，在整个过程中的cookie不会丢失

import requests
session = requests.session()
header = {
    "User-Agent": ":Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.58"
}
data = {
    "user_name": 18843501385,"user_pwd": "lzj110011"
}
# 登录
url = "http://www.zkk78.com/index.php/user/login.html"

resp = session.post(url=url,data=data,headers=header)
# print(resp.text)
# print(resp.cookies)
recp = session.get("http://www.zkk78.com/user/plays.html")
print(recp.text)

time.sleep(random.random()*20)
resp.close()
recp.close()