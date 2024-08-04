"""
Given two variables of integer type a and b, exchange their values without using a 
third temporary variable
"""

a=2
b=9
print("Before:",a,b)
a=a+b
b=a-b
a=a-b
print("After:",a,b)