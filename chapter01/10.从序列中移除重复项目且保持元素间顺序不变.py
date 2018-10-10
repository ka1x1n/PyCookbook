# -*- coding:utf-8 -*-
"""
问题：去除序列中出现的重复元素，但剩下的元素顺序不变
解决：如果序列中的值是可哈希的，可以通过集合和生成器解决
"""


def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


a = [1, 5, 2, 1, 9, 1, 5, 10]
print(list(dedupe(a)))  # [1, 5, 2, 9, 10]

# 如果序列中的元素 不可哈希：
def dedupe_unhashable(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)
# 这里参数key的作用是指定一个函数来将序列中的元素转换为可哈希的类型，目的是检测重复项

# 如果只是去除重复项，通常就是构建一个集合
set(a) # 不能保证顺序

