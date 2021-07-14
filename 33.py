# Write a Python program to create a dictionary of keys x, y, and z
# where each key has as value a list from 11-20, 21-30, and 31-40 respectively.
# Don’t use
# static value for 11-20, 21-30, 31-40. Access the fifth value of each key from the dictionary.
# Expected Output
# First
# x has value [11, 12, 13, 14, 15, 16, 17, 18, 19]
# y has value [21, 22, 23, 24, 25, 26, 27, 28, 29]
# z has value [31, 32, 33, 34, 35, 36, 37, 38, 39]
# Second
# 15
# 25
# 35


x={value:value for value in range(11,20)}
print(f" x has values{x.values()}")

y={value:value for value in range(21,30)}
print(f" y has values{y.values()}")

z={value:value for value in range(31,40)}
print(f" z has values{z.values()}")


m=list(x.keys())[4]
print(m)

n=list(y.keys())[4]
print(n)

o=list(z.keys())[4]
print(o)