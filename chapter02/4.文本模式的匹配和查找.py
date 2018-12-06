# -*- coding:utf-8 -*-

"""
问题：按照特定的文本模式进行匹配或查找
解决：字符串方法：str.find()、str.endswith()、str.startswith()
"""

import re

text = 'yeah, but no, but yeah, but no, but yeah'

print(text == 'yeah')
print(text.startswith('yeah'))
print(text.endswith('yeah'))
print(text.find('no'))  # 找到第一个no出现的位置

text1 = '11/28/2018'
text2 = 'Nov 28. 2018'

datepat = re.compile(r'\d+/\d+/\d+')

if re.match(datepat, text1):
    print('yes')
else:
    print('no')

if datepat.match(text2):
    print('yes')
else:
    print('no')

# 若想对整个文本搜索出所有的匹配项，应使用findall()方法
text3 = 'Today is 11/28/2018. starts 3/13/2013'
print(datepat.findall(text3))
datepat2 = re.compile(r'(\d+)/(\d+)/(\d+)')  # 捕获组，每个组的内容可以单独提取出来
print(datepat2.findall(text3))

m = datepat2.match('11/27/2018')
print(m)
print(m.group(0))
print(m.group(1))
print(m.groups())

# Find all matches
print(datepat2.findall(text3))
for month, day, year in datepat2.findall(text3):
    print('{}-{}-{}'.format(year, month, day))

# findall()方法搜索整个文本并找出所有的匹配项后将它们以列表的方式返回
# 若想以迭代的方式找出匹配项，可以使用finditer()方法
for m in datepat2.finditer(text3):
    print(m.groups())

# match()方法只会检查字符串的开头
# 若想精确匹配，确保在模式中包含一个结束标记$