#  -*- coding:utf-8 -*-
"""
问题：有一些很长的字符串，想将它们格式化，使得能够按照用户指定列数来显示
解决：textwrap模块来重新格式化文本的输出
"""
import os
import textwrap

s = "Look into my eyes, look into my eyes, the eyes, the eyes" \
    "the eyes, not around the eyes, don't look around the eyes," \
    "look into my eyes, you're under."

print(textwrap.fill(s, 80))
print(textwrap.fill(s, 40))
print(textwrap.fill(s, 40, initial_indent=' '))

# os.get_terminal_size()获取终端尺寸大小，为了更好的显示
print(os.get_terminal_size().columns)