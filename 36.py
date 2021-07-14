# Write a Python program to check if all values are the same in a dictionary.
# Original Dictionary:{'Cierra Vega': 23, 'Alden Cantrell': 23, 'Kierra Gentry': 23, 'Pierre Cox': 23}
# Check all are 23 in the dictionary.
# True
# Check all are 10 in the dictionary.
# False
#

# =======================================================
d= {'Cierra Vega': 23, 'Alden Cantrell': 23, 'Kierra Gentry': 23, 'Pierre Cox': 23}
def myfunc(d, n):
    result = all(x == n for x in d.values())
    return result
print(myfunc(d,23))
print(myfunc(d,10))

# ======================================================================================









