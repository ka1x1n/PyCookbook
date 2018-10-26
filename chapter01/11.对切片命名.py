# -*- coding:utf-8 -*-
"""
问题：清理硬编码的切片索引
解决：切片命名
"""

record = '.....100......513.25.....'
cost = int(record[5:8]) * int(record[14:17])  # 51300

# 以下为切片命名
SHARES = slice(5, 8)
PRICE = slice(14, 17)
slice_cost = int(record[SHARES]) * int(record[PRICE])  # 51300

# 硬编码的索引值导致可读性和可维护性不佳
# slice()函数会创建一个切片对象，用在任何允许进行切片操作的地方
items = [0, 1, 2, 3, 4, 5, 6]
a = slice(2, 4)
print(items[a])  # [2, 3]

items[a] = [10, 11]
print(items)  # [0, 1, 10, 11, 4, 5, 6]

del items[a]
print(items)  # [0, 1, 4, 5, 6]

# 如果有一个slice对象的实例s，可以分别通过s.start、s.stop、s.step属性来得到关于该对象的信息
a = slice(2, 5)
print(a.start)  # 2
print(a.stop)  # 4
print(a.step)  # None

# 此外可以使用indices(size)方法将切片映射到特定大小的序列上，返回一个(start,stop,step)元组
# 所有的值都恰当地限制在了边界内，避免做索引操作的时候出现IndexError
s = 'HelloWorld'
a.indices(len(s))
for i in range(*a.indices(len(s))):
    print(s[i])  # l l o