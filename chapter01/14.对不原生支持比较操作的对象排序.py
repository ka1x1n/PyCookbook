# -*- coding:utf-8 -*-
"""
问题：在同一个类的实例之间做排序，但是它们并不原生支持比较操作
解决：sorted()接受可调用对象key返回的对象的某些值进行排序
"""

from operator import attrgetter

class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id)

users = [User(23), User(3), User(99)]
print(users)
print(sorted(users, key=lambda u: u.user_id))

# 除了lambda， 另一种方式是operator.attrgetter

print(sorted(users, key=attrgetter('user_id')))
