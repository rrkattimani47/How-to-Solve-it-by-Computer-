"""
Design an algorithm that makes the following exchanges : 
a->b->c->a

The arrow indicates that b is to assume the value of a, c the value of b, and so on.
"""

a=10
b=2
c=88
print("Before : ",a,b,c)

temp=a
a=c
c=b
b=temp
print("After : ",a,b,c)
