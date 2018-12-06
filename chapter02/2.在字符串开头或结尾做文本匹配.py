# -*- coding:utf-8 -*-
"""
问题：在字符串的开头或结尾按照指定文本模式做检查，如扩展名、URL协议类型等
解决：str.startswith()
"""

import os, re

filename = 'readme.txt'
print(filename.endswith('txt'))
print(filename.startswith('file'))

url = 'http://www.baidu.com'
print(url.endswith('.com'))
print(url.startswith('www'))

filenames = os.listdir('.')
print(filenames)
print([name for name in filenames if name.endswith(('.py', '.c'))])

print(re.match('http:|https:|ftp:', url))


from urllib.request import urlopen


def read_data(name):
    choices = ['http:', 'https:', 'ftp:']
    if name.startswith(tuple(choices)):   #  需要把元组当成输入
        return urlopen(name).read()
    else:
        with open(name) as f:
            return f.read()


def main():
    result = read_data('http://www.baidu.com')
    print(result)


if __name__ == '__main__':
    main()