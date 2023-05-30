import time

from selenium.webdriver import Edge
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

web = Edge()
web.get("http://lagou.com")
time.sleep(1)
web.find_element(by=By.XPATH,value='//*[@id="changeCityBox"]/p[1]/a').click()
time.sleep(1)
web.find_element(by=By.XPATH,value='//*[@id="search_input"]').send_keys('python',Keys.ENTER)
time.sleep(1)
web.find_element(by=By.XPATH,value='//*[@id="openWinPostion"]').click()
time.sleep(1)
# 切换窗口
web.switch_to.window(web.window_handles[0])  # 跳转到最上排标签里第一个
time.sleep(2)
web.switch_to.window(web.window_handles[-1]) # 跳转到最上排标签里最后一个
time.sleep(2)
# 提取新窗口数据
description = web.find_element(by=By.XPATH,value='//*[@id="job_detail"]/dd[2]/div').text
print(description)
# 关闭当前窗口与
web.close()
# 切换到第几个窗口 （由于我只有；两个窗口，所以关掉一个窗口后没必要在切换到别的窗口）
# web.switch_to.window(web.window_handles[0])
 