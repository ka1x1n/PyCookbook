#  -*- coding:utf-8 -*-
"""
问题：用正则表达式处理文本，但是需要考虑处理Unicode字符
解决：可以针对Unicode字符使用转义序列
"""

import re
num = re.compile('\d+')
# ASCII digits
print(num.match('123'))
# Arabic digits
print(num.match('\u0661\u0662\u0663'))
