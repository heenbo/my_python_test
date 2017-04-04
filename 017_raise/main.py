#!/usr/bin/python3


#raise TypeError
class MyException(Exception):
    print("MyException action, hahahaha")


a = ['a', 'b', 'c', 'd']
b = [1, 2, 3, 4]
c = []

try:
    for i in a:
        for j in b:
            if i == 'b':
                raise MyException
            c.append([i, j])
except MyException:
    pass


print(c)
