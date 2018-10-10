#  -*-  coding:utf-8  -*-
"""
问题：有一个包含N个元素的元组或序列，分解为N个单独的变量
解决：复制操作来分解为单独的变量，唯一的要求是变量的总数和结构要与序列吻合
"""

p = (4, 5)
x, y = p
print(x)
print(y)

data = ['ACME', 50, 91.1, (2021, 12, 21)]
name, shares, price, date = data
print(name, shares, price, date)

name, shares, price, (year, month, day) = data
print(year, month, day)

s = 'HELLO'
a, b, c, d, e = s
print(a, b, c, d, e)

_, shares, price, _ = data
print(shares, price)