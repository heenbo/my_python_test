#!/usr/bin/python3


"""
mystr = "123456789"

for v in mystr:
    print(v)
    if v == '5':
        break

print("循环结束咯")
"""


mystr = "123456789"

for v in mystr:
    if v == '5':
       continue 
    print(v)

print("循环结束咯")
