#  -*- coding:utf-8 -*-

"""
问题：在字符串的开始、结尾或中间去掉不需要的字符，比如说空格符
解决：strip()方法可以在字符串的开始和结尾处去掉字符；lstrip()和rstrip()可分别从左、右驱虫
"""

# 这些方法默认去除空格符，但也可以指定其他字符

# Whitespace stripping
s = ' hello world \n'
print(s.strip())  # 'hello world'
print(s.lstrip())  # 'hello world \n'
print(s.rstrip())  # ' hello world'

# Character stripping
t = '-----hello====='
print(t.lstrip('-'))  # hello=====
print(t.rstrip('='))  # -----hello
print(t.strip('-='))  # hello

# strip()不会对字符串中间的文本做任何操作，需要其他技巧
m = ' hello    world   \n'
print(m.strip())  # 'hello    world'
print(m.replace(' ', ''))  # helloworld
import re
print(re.sub('\s+', ' ', m))  # \s 匹配空格符

