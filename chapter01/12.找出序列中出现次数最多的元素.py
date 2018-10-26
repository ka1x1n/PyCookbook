# -*- coding:utf-8 -*-
"""
问题：有一个元素序列，想知道出现次数最多的元素
解决：collections模块中的Counter类，其中的most_common()方法
"""

from collections import Counter

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    ',y', 'eyes', "you're", 'under'
]

word_counts = Counter(words)
top_three = word_counts.most_common(3)
print(top_three)  # [('eyes', 8), ('the', 5), ('look', 4)]
# 可以给Counter对象提供任何可哈希的对象序列作为输入。
# 底层实现：Counter是一个字典，在元素和次数间做了映射

print(word_counts['not'])

# 如果想手动增加计数：1.自增 2.update()方法
morewords = ['why', 'are', 'you', 'not', 'looking', 'in', 'my', 'eyes']
for word in morewords:
    word_counts[word] += 1

word_counts.update(morewords)

# Counter对象可以和各种数学运算操作结合
a = Counter(words)
b = Counter(morewords)
c = a + b
d = a - b