#  -*- coding:utf-8 -*-
"""
问题：对字符串中的文本做查找和替换
解决：对于简单的文本模式，使用str.replace()；对于复杂的，使用re中的sub()方法；
"""

text = 'yeah, but no, but yeah, but no, but yeah'
print(text.replace('yeah', 'yep'))

import re
text2 = 'Today is 11/28/2018. starts 3/13/2013'
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
print(re.sub(datepat, r'\3-\1-\2', text2))

# 对于更复杂的模式，可以指定一个替换回调函数
from calendar import month_abbr
def change_date(m):
    mon_name = month_abbr[int(m.group(1))]
    return '{} {} {}'.format(m.group(2), mon_name, m.group(3))

print(datepat.sub(change_date, text2))