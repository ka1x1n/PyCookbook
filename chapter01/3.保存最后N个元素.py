#    -*- coding:utf-8 -*-
"""
问题：对最后几项做一个有限的历史记录统计
解决：collections.deque
"""

from collections import deque


def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)#deque当有新的记录加入而队列已满时会自动移出最老的记录
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)


if __name__ == '__main__':
    with open('somefile.txt') as f:
        for line, prevlines in search(f, 'python', 5):
            for pline in prevlines:
                print(pline, end='')
                print('-'*20)