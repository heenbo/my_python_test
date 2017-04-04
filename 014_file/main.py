#!/usr/bin/python3
#coding:utf-8

"""
#coding:utf-8


#f = open('test.txt', 'rw', encoding='utf-8')
f = open('test.txt', 'r+', encoding='utf-8')


"""
#f.write('hello world 我是贺贺\n')
"""

print(f.readline())


f.close()
"""

#with open('test.txt', 'r+', encoding='utf-8') as f:
with open('test.txt', 'r+') as f:
    for v in f:
        print(f.read(), end="")
