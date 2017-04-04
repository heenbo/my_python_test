#!/usr/bin/python3

"""
*args:无组的方式
*kwargs:字典的形式
"""

def my_func(name="猪", *args, **kwargs):
    print("hello world, function test OK")
    print("我是%s"% name)
    print("args:")
    print(args)
    print(kwargs)
    return name

input_str = input("你的名字是：")

if len(input_str) <= 0:
    my_func()
else:
    my_func(input_str, 22, 33, 44, sex='男', abc="aaa")


print("=====================================")

result = my_func("afasdfa")
print(result)
