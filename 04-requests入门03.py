import requests

# 这条代码也一样能运行
# url = 'https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A90&action=&start=0&limit=20'
url = 'https://movie.douban.com/j/chart/top_list'

param = {
    'type': '24',
    'interval_id': '100:90',
    'action': '',
    'start': 0,
    'limit': 20,
}

heard = {
    'User-Agent':':Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.48'
}

# 在post请求中 封装内容用datas 而get中 用params
rest = requests.get(url=url,params=param,headers=heard)
print(rest.json())
rest.close()