#  -*- coding:utf-8 -*-
"""
问题：以某种方式对齐方式将文本做格式化处理
解决：ljust()、rjust()和center()方法
"""

text = 'Hello World'
print(text.ljust(20))
print(text.rjust(20))
print(text.center(20))

# 所有方法都接受一个可选的填充字符
print(text.rjust(20, '='))
print(text.ljust(20, '*'))
print(text.center(20, '^'))

# format()也可，需要做的就是合理利用 < > ^ 和一个期望值
print(format(text, '>20'))
print(format(text, '<20'))
print(format(text, '*^20'))

# 当格式化多个值，格式化代码也可以用在format()方法中
print('{:>10s} {:>10s}'.format('Hello', 'World'))