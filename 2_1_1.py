"""
Given two glasses marked A and B Glass is full of Raspberry drink and glass B is full of lemonade. 
Suggest a way of exchanging the contents of glasses A and B.
"""

a="raspberry drink"
b="lemonade"

print("Before Exchange")
print("Glass A ", a)
print("Glass B ", b)

temp=a
a=b
b=temp

print("\nAfter exchange")
print("Glass A ", a)
print("Glass B ", b)