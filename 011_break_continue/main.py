#!/usr/bin/python3


"""
mystr = "123456789"

for v in mystr:
    print(v)
    if v == '5':
        break

print("循环结束咯")
"""

"""
mystr = "123456789"

for v in mystr:
    if v == '5':
       continue 
    print(v)

print("循环结束咯")
"""

a = ['a', 'b', 'c', 'd']
b = [1, 2, 3, 4, 5, 6]
c = []

for i in a:
    for j in b:
        if i == 'b':
            break
        c.append([i,j])

print("循环结束咯")
print(c)
d = len(c)
print("d:%d"%(d))

