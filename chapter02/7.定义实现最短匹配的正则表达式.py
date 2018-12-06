# -*- coding:utf-8 -*-
"""
问题：找出最短的可能匹配
解决：只要在模式中的*操作符后加上?修饰符
"""

import re
str_pat = re.compile(r'\"(.*)\"')
text1 = 'Computer says "no."'
print(str_pat.findall(text1))  # ['no.']

text2 = 'Computer says "no." Phone says "yes."'
print(str_pat.findall(text2))  # ['no." Phone says "yes.']

# *操作符在正则表达式中采用的是贪心策略，所以匹配过程是基于找出最长的可能匹配来进行的
# 在*操作符后加上?操作符即可解决
str_pat1 = re.compile(r'\"(.*?)\"')
print(str_pat1.findall(text2))