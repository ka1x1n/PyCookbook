# -*- coding:utf-8 -*-
"""
问题：将字符串拆分为不同的字段，但是分隔符在整个字符串中并不一致
解决：字符串对象的split()方法可以处理简单的，但是不支持多个分隔符；使用re.split()方法
"""

import re

line = 'asdf fjdk; afed, fjek, asdf,   foo'
print(re.split(r'[;,\s]\s*', line))

fields = re.split(r'(;|,|\s)\s*', line)
print(fields)

values = fields[::2]
delimiters = fields[1::2] + ['']
print(values)
print(delimiters)
print(''.join(v+d for v, d in zip(values, delimiters)))

print(re.split(r'(?:,|;|\s)\s*', line))