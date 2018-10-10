# -*- coding:utf-8 -*-
"""
问题：创建一个字典，对字典做迭代或序列化操作时，控制其中元素顺序
解决：colletions模块中的OrderedDist类
"""

from collections import OrderedDict

d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4

for key in d:
    print(key, d[key])

# 当构建一个映射结构以便对其做序列化或编码成另一种格式时，OrderedDict就特别有用
# 例如，想在JSON编码时精确控制各字段顺序时
import json
json.dumps(d)

# OrderedDcit内部维护了一个双向链表，根据元素加入顺序来排列键的位置
# 第一个新加入的元素被放置在链表的末尾，对已存在的键重新赋值不会改变键的顺序
# 注：OrderedDict的大小是普通字典的2倍，这是由于额外创建的链表导致

