# -*-coding:utf-8 -*-
"""
问题：通过名称来访问元素，以此减少结构中对位置的依赖性
解决：collections.namedtuple()是一个工厂方法，返回Python中标准元组类型的子类
"""

from collections import namedtuple

Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('jonesy@example.com', '2012-10-19')
print(sub)
print(sub.addr, sub.joined)

# namedtuple的实例与普通的元组是可以互换的，且支持所有普通元组所支持的操作，例如索引和分解
print(len(sub))
addr, joined = sub
print(addr, joined)

# 命名元组的主要作用自傲与将代码同它控制的元素位置间解耦
# 如果从数据库调用中得到一个大型的元组列表，且通过位置访问数据，如果新增数据则会造成代码崩溃

def old_compute_cost(records):
    total = 0.0
    for rec in records:
        total += rec[1] * rec[2]
    return total

Stock = namedtuple('Stock', ['name', 'shares', 'price'])
def new_compute_cost(records):
    total = 0.0
    for rec in records:
        s = Stock(*rec)
        total += s.shares *s.price
    return total