# -*- coding:utf-8 -*-
"""
问题：在字典上对数据进行各式各样的计算（求最小、最大、排序等）
解决：zip()、sorted()
"""

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

# 利用zip()反转键值
min_price = min(zip(prices.values(), prices.keys()))
# min_price is (10.75, 'FB')
max_price = max(zip(prices.values(), prices.keys()))
# max_price is (612.78, 'AAPL')

# 对数据进行排序只需要zip()配合sorted()即可
prices_sorted = sorted(zip(prices.values(), prices.keys()))
# [(10.75, 'FB'), (37.2, 'HPQ'), (45.23, 'ACME'), (205.55, 'IBM'), (612.78, 'AAPL')]

# zip()创建了一个迭代器，内容只可以被消费一次