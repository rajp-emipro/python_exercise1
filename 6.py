# 6}Write a Python program to calculate the sum of three given numbers,
# if the values are equal then return three times of their sum.

def myfunc1(a,b,c):
    if a == b == c:
        return (a+b+c)*3
     else:
         return a+b+c
print(myfunc1(1,1,1))
print(myfunc1(2,3,6))
