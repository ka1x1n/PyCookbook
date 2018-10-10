# -*- coding:utf-8 -*-
"""
问题：在两个字典中，寻找相同的地方
解决：keys()或者items()方法
"""

a = {
    'x': 1,
    'y': 2,
    'z': 3
}

b = {
    'w': 10,
    'x': 11,
    'y': 2
}

# Find keys in common
a.keys() & b.keys()  # {'x', 'y'}

# Find keys in a that are not in b
a.keys() - b.keys()  # {'z'}

# Find (key,value) pairs in common
a.items() & b.items()  # {('y', 2)}

# 引申：可以用来修改或过滤字典内容
# 例如：假设创建一个新字典，去掉其中某些键
c = {key:a[key] for key in a.keys() - {'z', 'w'}}  # c is {'y': 2, 'x': 1}
