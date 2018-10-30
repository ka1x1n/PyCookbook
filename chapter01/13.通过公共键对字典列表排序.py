# -*- coding:utf-8 -*-
"""
问题：有一个字典列表，根据一个或多个字典中的值来对列表排序
解决：利用operator模块中的itemgetter函数
"""

from operator import itemgetter

rows = [
    {'fname': 'Brain', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

# sorted()接受一个关键字参数key，代表一个可调用对象。
# itemgetter()创建的就是这样一个可调用对象

rows_by_fname = sorted(rows, key=itemgetter('fname'))
rows_by_uid = sorted(rows, key=itemgetter('uid'))

print(rows_by_fname)
print(rows_by_uid)
