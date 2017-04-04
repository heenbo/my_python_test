#!/usr/bin/python3

"""
try:
    <code>
except <exception name>
    <code>
except <>,<>:
    <code>
else:
    <code>
finally:
    <code>
"""

try:
    a = input("请输入数字")
    b = int(a)
except ValueError as e:
    print('有异常',e)
else:
    print("没有异常")
finally:
    print("反正会执行")


