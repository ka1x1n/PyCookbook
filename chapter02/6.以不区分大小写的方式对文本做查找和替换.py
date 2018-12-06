#  -*- coding:utf-8 -*-
"""
问题：以不区分大小写的方式对文本做查找和替换
解决：使用re模块中并且对各种操作都要加上re.IGNORECASE标记
"""
import re

text = 'UPPER PYTHON, lower python, Mixed Python'
print(re.findall('python', text, flags=re.IGNORECASE))

# 局限：待替换的文本与匹配的文本大小写并不吻合，需要用到一个支撑函数(support function)
def matchcase(word):
    def replace(m):
        text = m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word
    return replace
print(re.sub('python', matchcase('snake'), text, flags=re.IGNORECASE))