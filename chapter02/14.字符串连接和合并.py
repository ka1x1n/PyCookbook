#  -*- coding:utf-8 -*-
"""
问题：将许多小字符串合并成一个大字符串
解决：join()方法
"""

parts = ['Is', 'Chicago', 'Not', 'Chicago?']
print(' '.join(parts))
print(','.join(parts))
print('*'.join(parts))

# 如果只是想连接一些字符串，+ 就可以完成,对于大量工作来说效率非常低
a = 'Is Chicago'
b = 'Not Chicago?'
print(a + ' ' + b)

print('{} {}'.format(a, b))

# 利用生成器表达式在数据转换为字符串的同时完成连接操作
data = ['ACME', 50, 91.1]
print(','.join(str(d) for d in data))

print(a, b, sep=':')

# 通过yield关键字生成字符串片段
def sample():
    yield 'Is'
    yield 'Chicago'
    yield 'Not'
    yield 'Chicago?'


print(' '.join(sample()))
