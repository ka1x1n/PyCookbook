#  -*- coding:utf-8 -*-
"""
问题：确保所有的字符串都有相同的底层表示
解决：unicodedata模块
"""

import unicodedata

s1 = 'Spicy Jalape\u00f1o'
s2 = 'Spicy Jalapen\u0303o'
print(s1, '\n'+s2)
print(s1 == s2)

# normalize()的第一个参数指定了字符串应该如何完成规范表示
# NFC表示字符应该是全组成的，NFD表示应该使用组合字符
t1 = unicodedata.normalize('NFC', s1)
t2 = unicodedata.normalize('NFC', s2)
print(t1 == t2)
