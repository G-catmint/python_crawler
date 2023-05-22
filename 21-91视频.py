import random
import time
import cchardet
import requests
import base64
from Crypto.Cipher import AES

url = "https://www.hxaa120.com/#/moves/playvideo/30847"
url_video = "https://zms.mw30su.cn/DM1269TUR/hls/CCvUW8P2.ts?auth_key=1682765564-0-0-3dfd07096f70291e1247925663208906"
url_key = "https://zms.mw30su.cn/DM1269TUR/hls/key.key?auth_key=1682765564-0-0-5fa3ac665fe5edc26ac55d22f2b4af62"

header = {
    "origin": "https://www.hxaa120.com",
    "referer": "https://www.hxaa120.com/",
    # "sec-ch-ua-mobile": "?0",
    "content-type": "charset=utf8",
    # "sec-ch-ua-platform": "Windows",
    # "sec-fetch-dest": "empty",
    # "sec-fetch-mode": "cors",
    # "sec-fetch-site": "cross-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.64"
}

resp = requests.get(url=url_video,headers=header)
with open("视频/3.mp4",mode="wb") as f:
    f.write(resp.content)
    print("完成")



resp1 = requests.get(url_key)
resp1_text = resp1.text.encode("utf-8")
print(resp1_text)
print(type(resp1_text))
aes = AES.new(key=resp1_text, IV=b"0000000000000000", mode=AES.MODE_CBC)
with open("视频/3.mp4",mode="rb")as f1:
    with open("视频/temp_3.mp4",mode="wb") as f2:
        bs = f1.read()
        f2.write(aes.decrypt(bs))

resp1.close()



time.sleep(random.random()*5)
resp.close()