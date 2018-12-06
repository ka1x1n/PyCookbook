#  -*- coding:utf-8 -*-
"""
问题：将&entity或&#code这样的HTML或XML实体替换为对应的文本；或对期望的文本进行特定字符转义
解决：使用html.escape()函数替换<or>这样的特殊字符
"""

import html

s = 'Element are written as "<tag>text</tag>".'
print(s)
print(html.escape(s))

# Disable escaping of quotes
print(html.escape(s, quote=False))

# 如果要生成ASCII文本，并且想针对非ASCII字符将它们对应的字符编码实体嵌入到文本中，可以在各种同I/O相关的函数中使用
# errors='xmlcharrefreplace'参数来实现
s = 'Spicy &quot; Jalape&#241;o&quot.'
print(html.unescape(s))
