#  -*- coding:utf-8 -*-
"""
问题：用正则表达式对一段文本块做匹配，能够跨多行
解决：添加对换行符的支持
"""

import re
comment = re.compile(r'/\*(.*?)\*/')
text1 = '/* this is a comment */'
text2 = """/* this is a 
            multiline comment */"""
print(comment.findall(text1))  # [' this is a comment ']
print(comment.findall(text2))  # []

# 要解决这个问题，(?:.|\n)指定了一个非捕获组（即只做匹配不做捕获）
comment1 = re.compile(r'/\*((?:.|\n)*?)\*/')
print(comment1.findall(text2))  # [' this is a \n            multiline comment ']

# re.compile()函数可接受一个有用的标记--re.DOTALL，使得正则表达式中的句点可以匹配所有字符，包括换行符
comment2 = re.compile(r'/\*(.*?)\*/', re.DOTALL)
print(comment2.findall(text2))  # [' this is a \n            multiline comment ']
