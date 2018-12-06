#  -*- coding:utf-8 -*-
"""
问题：字节串(Byte String)上执行常见的文本操作(拆分，替换，搜索)
解决：1.內建操作；2.正则表达式的模式匹配
"""

data1 = b'Hello World'
print(data1[0:5])  # b'Hello'
print(data1.startswith(b'Hello'))  # True
print(data1.split())  # [b'Hello', b'World']
print(data1.replace(b'Hello', b'Hello Cruel'))  # b'Hello Cruel World'

# 类似操作在字节数组上也能完成
data2 = bytearray(b'Hello World')
print(data2[0:5])  # bytearray(b'Hello')
print(data2.startswith(b'Hello'))  # True

# 正则表达式的模式匹配，但是模式本身需要以字节串的形式指定
data = b'FOO:BAR,SPAM'
import re
#print(re.split('[:,]', data))  # 出错
print(re.split(b'[:,]', data))  # [b'FOO', b'BAR', b'SPAM']

# 讨论
a = 'Hello'
b = b'Hello'
print(a[0])  # H
print(b[0])  # 72
# 字节串解码为文本字符串，字节串没有普通字符串的格式化操作
print(b)  # b'Hello'
print(b.decode('ascii'))  # Hello