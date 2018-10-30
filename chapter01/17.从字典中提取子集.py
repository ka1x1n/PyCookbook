# -*- coding:utf-8 -*-
"""
问题：创建一个字典，其本身是另一个字典的子集
解决：字典推导式(dicitonary comprehension)
"""

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

# Make a dictionary of all prices over 200
p1 = {key:value for key, value in prices.items() if value > 200}
print(p1)
# Make a dictionary of tech stocks
tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
p2 = {key:value for key, value in prices.items() if key in tech_names}
print(p2)