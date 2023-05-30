import time

from selenium.webdriver import Edge
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.options import Options

# 无可视化界面设置 #

edge_options = Options()
# 使用无头模式
edge_options.add_argument('--headless')
# 禁用GPU，防止无头模式出现莫名的BUG
edge_options.add_argument('--disable-gpu')

# 将参数传给浏览器
web = Edge(options=edge_options)
web.get("http://lagou.com")
el = web.find_element(by=By.XPATH, value='//*[@id="changeCityBox"]/p[1]/a')
el.click()
ele = web.find_element(by=By.XPATH,value='//*[@id="search_input"]').send_keys('python',Keys.ENTER)
time.sleep(5)
li_list = web.find_elements(by=By.XPATH,value='//*[@id="jobList"]/div[1]/div')
for li in li_list:
    li_name = li.find_element(by=By.XPATH,value='./div[1]/div[1]/div[1]/a').text
    li_price = li.find_element(by=By.XPATH,value='./div[1]/div[1]/div[2]/span').text
    li_compiny = li.find_element(by=By.XPATH,value='./div[2]/div[1]').text
    print(li_compiny,li_name,li_price)
