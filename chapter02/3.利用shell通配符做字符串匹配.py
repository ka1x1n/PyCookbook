# -*- coding:utf-8 -*-

"""
问题：当工作在UNIX shell时，我们想使用常见的通配符模式来对文本匹配
解决：fnmatch模块提供了两个函数 fnmatch()和fnmatchcase()可以执行这样的匹配
"""

from fnmatch import fnmatch, fnmatchcase

print(fnmatch('too.txt', '*.txt'))
print(fnmatch('foo.txt', '?oo.txt'))
print(fnmatch('Dat45.csv', 'Dat[0-9]*'))

names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
print([name for name in names if fnmatch(name, 'Dat*.csv')])

#  fnmatch()根据操作系统 区分是否大小写
#  fnmatchcase() 区分匹配的大小写

print(fnmatch('foo.txt', '*.TXT'))
print(fnmatchcase('foo.txt', '*.txt'))

addresses = [
    '5412 N CLARK ST',
    '1060 W ADDISON ST',
    '1039 W GRANVILLE AVE',
    '2122 N CLARK ST',
    '4802 N BROADWAY',
]

print([addr for addr in addresses if fnmatchcase(addr, '* ST')])
print([addr for addr in addresses if fnmatchcase(addr, '54[0-9][0-9] *CLARK*')])