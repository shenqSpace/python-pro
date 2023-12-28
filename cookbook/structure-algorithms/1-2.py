"""
从任意长度的可迭代对象中分解元素
"""
import math


def drop_first_last(grades):
    first, *middle, last = grades
    return math.avg(middle)

record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *numbers = record
print('name is', name, 'eamil is', email)
print(numbers)


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
        

"""
做某些特定字符串拆分时, *也很管用
"""
line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')

# 对于我们不想要的值直接用 _ 来替代
uname2, *_, homedir2, sh2 = line.split(':')

