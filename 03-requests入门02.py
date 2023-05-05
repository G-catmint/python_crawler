import requests
url = 'https://fanyi.baidu.com/sug'

world = input("输入你想要翻译的话")

data = {
    'kw': 'world'
}

# 发送post请求
result = requests.post(url,data=data)
print(result.json())# 将服务器返回的内容直接处理成josn() ->dict
result.close()