import re

# re.findall(匹配规则，被匹配字符串)
# 匹配整个字符串,找出全部匹配项
# reach_findall = re.findall("\d+","我的电话号是10086，女朋友的电话是10010")
# print(reach_findall)
#
# # finditer：匹配字符串中所有内容[返回迭代器]
# reach_finditer = re.finditer("\d+","我的电话号是10086，女朋友的电话是10010")
# for i in reach_finditer:
#     print(i.group())# 10086
#                     # 10010


# re.search(匹配规则，被匹配字符串)
# 搜索整个字符串,找出匹配的。从前向后,找到第一个后，就停止,不会继续向后
# reach_search = re.search(r"\d+","我的电话号是10086，女朋友的电话是10010")
# print(reach_search.group())

# # re.match(匹配规则，被匹配字符串)
# # 从被匹配字符串开头进行匹配，匹配成功返回匹配对象(包括匹配信息),匹配不成功则返回空
# # reach_match = re.match(r"\d+","我的电话号是10086，女朋友的电话是10010")
# reach_match = re.match(r"\d+","10086，女朋友的电话是10010")
# print(reach_match.group())

# # 预加载正则表达式
# obj = re.compile("\d+")
# of = obj.findall("我的电话号是10086，女朋友的电话是10010")
# for i in of:
#     print(i)

# s = """
# <div class='Marie Rose'><span id='1'>玛莉萝丝</span></div>
# <div class='Honoka'><span id='2'>穗香</span></div>
# <div class='Kasumi'><span id='3'>霞</span></div>
# <div class='Misaki'><span id='4'>海咲</span></div>
# <div class='Nyotengu'><span id='5'>女天狗</span></div>
# """
# # (?P<分组名>正则) 可以单独从正则匹配中进一步提取内容
# obj = re.compile(r"<div class='(?P<AzurLane>.*?)'><span id='(?P<ID>\d+)'>(?P<yahaha>.*?)</span></div>",re.S) # re.S让 . 能匹配换行符
# reach= obj.finditer(s)
# for it in reach:
#     print(it.group("yahaha"),end=' ')
#     print(it.group("ID"),end=' ')
#     print(it.group("AzurLane"))