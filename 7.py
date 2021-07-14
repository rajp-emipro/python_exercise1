# 7}Write a Python program to get a string
# which is n (non-negative integer) copies of a given string.

def cpy(str,n):
   total = ""
   for i in range(n):
      total = total + str
   return total
str=input("enter the string:")
n=int(input("enter no of times you want to repeat string:"))
print(cpy(str, n))
