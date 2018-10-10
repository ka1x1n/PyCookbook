# -*- coding:utf-8 -*-
"""
问题：实现一个队列，以给定的优先级对元素排序，且每次pop都会返回优先级最高的元素
解决：heapq模块
"""

import heapq


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)


def main():
    q = PriorityQueue()
    q.push(Item('foo'), 1)
    q.push(Item('bar'), 5)
    q.push(Item('spam'), 4)
    q.push(Item('grok'), 1)
    print(q.pop())
    print(q.pop())
    print(q.pop())
    print(q.pop())

if __name__ == '__main__':
    main()# -*- coding:utf-8 -*-
"""
问题：实现一个队列，以给定的优先级对元素排序，且每次pop都会返回优先级最高的元素
解决：heapq模块
"""

import heapq


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))  #取负是为了让队列能够按元素的优先级从高到低排序
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)


def main():
    a = (1, Item('foo'))
    b = (5, Item('bar'))
    c = (1, Item('gork'))
    q = PriorityQueue()
    q.push(Item('foo'), 1)
    q.push(Item('bar'), 5)
    q.push(Item('spam'), 4)
    q.push(Item('grok'), 1)
    print(q.pop())
    print(q.pop())
    print(q.pop())
    print(q.pop())
    print(a < b)
    print(a < c)  # 报错

if __name__ == '__main__':
    main()