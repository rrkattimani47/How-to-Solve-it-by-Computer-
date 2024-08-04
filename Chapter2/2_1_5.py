"""
What happens when the argument given to the procedure exchange are i and a[i]?
"""

def exchange(i, value):
    a[i] = i
    print(a[i])

a = [10, 20, 30, 40, 50]
exchange(2, a[2])
print("After Swap",a)

