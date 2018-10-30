# -*- coding:utf-8 -*-
"""
问题：有多个字典或映射，在逻辑上将它们合并为一个单独的映射结构
解决：collecitons模块中的ChainMap
"""

from collections import ChainMap

a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}

c = ChainMap(a, b)  # 先在a找，没有则去b找
print(c['x'])  # Outputs 1 from a
print(c['y'])  # Outputs 2 from b
print(c['z'])  # Outputs 3 from a

# ChainMap 这些映射在字面上并不会合并在一起
# 相反，其只是简单地维护一个记录底层映射关系的列表，然后重定义长江的字典操作来扫描这个列表

# ChainMap 与带有作用域的值，比如变量一起工作时特别有用
values = ChainMap()
values['x'] = 1
# Add a new mapping
values = values.new_child()
values['x'] = 2
# Add a new mapping
values = values.new_child()
values['x'] = 3
print(values)
# Discard last mapping
values = values.parents
print(values)