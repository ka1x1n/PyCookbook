# -*- coding:utf-8 -*-
"""
问题：序列中的数据根据某些标准进行删减
解决：列表推导式(list comprehension)
"""

mylist = [1, 4, -5, 10, -7, 2, 3, -1]
print([n for n in mylist if n > 0])
print([n for n in mylist if n < 0])

# 缺点：如果原始输入非常大，结果不理想
# 改进：使用生成器表达式通过迭代的方式产生筛选结果

pos = (n for n in mylist if n > 0)
for x in pos:
    print(x)

# 问题：筛选标准有时无法简单地表示在列表推导式或生成器表达式中
# 解决：将处理筛选的代码放在单独的函数中，利用內建的filter()函数处理

values = ['1', '2', '-3', '-', '4', 'N/A', '5']

def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False


ivals = list(filter(is_int, values))  # filter()创建了一个迭代器，如果我们希望结果是列表则需要list()
print(ivals)

# 讨论： 利用列表推导式或生成器表达式来筛选数据是最简单直接的方式

clip_neg = [n if n > 0 else 0 for n in mylist]  # 不满足条件则替代
print(clip_neg)

# 另一个筛选工具：itertools.compress()，接受一个可迭代对象以及一个布尔选择器序列作为输入
# 输出时，它会给出所有在相应的布尔选择器中为True的可迭代对象元素

address = [
    '5412 N CLARK',
    '5148 N CLARK',
    '5800 E 58TH',
    '2122 N CLARK',
    '5645 N RAVENSWOOD',
    '1060 W ADDISON',
    '4801 N BROADWAY',
    '1039 W GRANVILLE',
]

counts = [0, 3, 10, 4, 1, 7, 6, 1]

from itertools import compress

more5 = [n > 5 for n in counts]
print(list(compress(address, more5)))

