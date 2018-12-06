#  -*- coding:utf-8 -*-

"""
问题：创建一个字符串，其中嵌入的变量名称以变量的字符串值形式替换掉
解决：Python并不直接支持在字符串中的对变量做简单的值替换，但是可以通过format()近似模拟出来
"""

s = '{name} has {n} messages.'
print(s.format(name='Guido', n=37))

# 另一种方式是，如果要被替换的值能在变量中找到，则可以将format_map()和vars()联合使用
name = 'Guido'
n = 37
print(s.format_map(vars()))

# 有关vars()一个特性也能作用与类实例上
class Info():
    def __init__(self, name, n):
        self.name = name
        self.n = n

a = Info('Guido', 37)
print(s.format_map(vars()))  # Guido has 37 messages.

# format()和format_map()缺点在于无法处理缺少一个值的情况
# 为了避免此类情况，可单独定义一个带有__missing_()方法的字典类
class safesub(dict):
    def __missing__(self, key):
        return '{' + key + '}'

del n
print(s.format_map(safesub(vars())))  # Guido has {n} messages.
