# -*- coding:utf-8 -*-
"""
问题：一键多值的字典
解决：将多个值保存到另一个容器如列表或集合中
"""
#要使用列表还是集合取决于应用的意图
#如果希望保留元素插入顺序：列表
#如果希望消除重复元素：集合

d = {
    'a': [1,2,3],
    'b': [4,5],
}

e = {
    'a': {1,2,3},
    'b': {4,5}
}

#为了方便创建这样的字典，可以利用collections模块中的defaultdict类
#defaultdict的特点就是它会初始化第一个值，只需要关注添加元素即可
from collections import defaultdict

a = defaultdict(list)
a['a'].append(1)
a['d'].append(2)

for key,value in pairs:
    d[key].append(value)