"""
Design an algorithm that makes the following exchanges:
a->b->c->d->a
"""

a=11
b=12
c=13
d=14
print("Before",a,b,c,d)
temp = a
a = d
d = c
c = b
b = temp
print("After: ",a,b,c,d)