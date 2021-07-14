# Write a Python program to multiply all the items in a list.

# def myfunc(list1):
#     mult=1
#     for x in list1:
#         mult = mult *x
#     return mult
# print(myfunc([1,2,3,4]))

# import math
# list1 = [1, 2, 3, 4]
# print(math.prod(list1))

from functools import reduce
z=reduce(lambda x, y: x*y, [1,2,3,4,5,6])
print(z)

