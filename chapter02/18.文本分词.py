#  -*- coding:utf-8 -*-
"""
问题：有一个字符串，想从左到右将它解析为标记流(stream of tokens)
解决：对字符串做分词处理，匹配模式。利用正则表达式中的命名捕获组
"""

text = 'foo = 23 + 42 * 10'

tokens = [('NAME', 'foo'), ('EQ', '='), ('NUM', '23'),
          ('PLUS', '+'), ('NUM', '42'), ('TIMES', '*'), ('NUM', '10')]

import re
NAME = r'(?P<NAME>[a-zA-Z_0-9]*)'
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
TIMES = r'(?P<TIMES>\*)'
EQ = r'(?P<EQ>=)'
WS = r'(?P<WS>\s+)'
# ?P<TOKENNAME>将名称分配给该模式

master_pat = re.compile('|'.join([NAME, NUM, PLUS, TIMES, EQ, WS]))

# 接下来使用模式对象的scanner()方法完成分词操作。
# 该方法创建一个扫描对象，在给定的文本中重复调用match()，一次匹配一个模式
scanner = master_pat.scanner('foo = 42')
print(scanner.match())

# 包含在生成器函数中
from collections import namedtuple

Token = namedtuple('Token', ['type', 'value'])

def generate_tokens(pat, text):
    scanner = pat.scanner(text)
    for m in iter(scanner.match, None):
        yield Token(m.lastgroup, m.group())

# Example use
for tok in generate_tokens(master_pat, 'foo = 42'):
    print(tok)
# produces output:
# Token(type='NAME', value='foo')
# Token(type='NAME', value='')
# Token(type='NAME', value='')
# Token(type='NAME', value='')
# Token(type='NAME', value='42')
# Token(type='NAME', value='')

# 第一步分词，对于每个可能出现的文本序列，需要确保有一个对应的模式将其识别。如果不能识别，则停止扫描。
# 所以定义WS指定空格标记
# 标记在正则表达式的顺序也很重要，re模块会按照指定顺序对模式进行匹配