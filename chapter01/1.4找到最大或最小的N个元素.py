# -*- coding:utf-8 -*-
"""
问题：在某个集合中找出最大或最小的N个元素
解决：heapq模块有两个函数：nlargest()和nsmallest()
"""

import heapq

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3,nums))
print(heapq.nsmallest(3,nums))

# 这两个函数可以接受参数key，从而工作在更复杂的数据结构上
portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 43, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]

cheap = heapq.nsmallest(1, portfolio, key=lambda s: s['price'])
expensive = heapq.nlargest(1, portfolio, key=lambda s: s['price'])
print(cheap)
print(expensive)