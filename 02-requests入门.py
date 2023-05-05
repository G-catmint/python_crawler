# 安装requests
# pip install requests

import requests
wd = input("输入你想搜索的内容")

url = f'http://www.baidu.com/s?wd={wd}'

headers = {
    "User-Agent":":Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.48"
}

rest = requests.get(url,headers=headers)
print(rest.text)
rest.close()