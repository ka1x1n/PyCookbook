#    -*- coding:utf-8    -*-
"""
问题：需要从某个可迭代对象中分解出N个元素，单此对象可能长度超过N，会导致出现“分解的值过多”的异常
解决：“表达式”可以解决这个问题
"""


def drop_first_last(grades):
    first, *middle, last = grades
    return avg(middle)             #  对中间的分数求平均

record = ('Dengkaixin', 'dkx@NELWS.com', '136-5919-7499', '1234567')
name, mail, *phone_numbers = record
print(name, mail, phone_numbers)

*trailing_qtrs, current_qtr = [10, 5, 4, 2, 1, 7, 8, 6]
trailing_avg = sum(trailing_qtrs) / len(trailing_qtrs)
print(trailing_avg)
print(current_qtr)


records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4)
]


def do_foo(x, y):
    print('foo', x, y)


def do_bar(s):
    print('bar', s)


for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)

line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')
print(uname, homedir, sh)


record = ('ACME', 50, 123.45, (12, 18, 2012))
name, *_, (*_, year) = record
print(name, year)


items = [1, 3, 5, 7, 9]
head, *tail = items
print(head, tail)


def sum(items):
    head, *tail = items
    return head + sum(tail) if tail else head

print(sum(items))