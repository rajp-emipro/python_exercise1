# 5}Write a Python program to get the difference between
# a given number and 17, if the number is greater than 17 return double the absolute difference.

def diff(x):
    if x<17:
        return 17-x
    else:
        return abs((x-17)*2)
num=int(input("the number you want to subtract from 17:"))
print(diff(num))
