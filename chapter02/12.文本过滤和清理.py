#  -*- coding:utf-8 -*-
"""
问题： 文本过滤与清理
解决： str.replace()、re.sub()、str.translate()等方法
"""

import unicodedata, sys

s = 'python\fis\tawesome\r\n'
print(s)

# 第一步 清理空格：先建立小型转换表，使用translate()方法
remap = {
    ord('\t'): ' ',
    ord('\f'): ' ',
    ord('\r'): None   # Deleted
}
a = s.translate(remap)
print(a)
# 第二步 去掉所有Unicode组合字符
cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode) if unicodedata.combining(chr(c)))
b = unicodedata.normalize('NFD', a)
print(b)
print(b.translate(cmb_chrs))


# 对于简单的替换操作，str.replace()通常是最快的方式
def clean_spaces(s):
    s = s.replace('\r', '')
    s = s.replace('\t', '')
    s = s.replace('\f', '')
    return s