# Write a Python program to count the number of strings in a list
# where the string length is 2 or more and the first and last character are the same
# from a given list of strings.
ls=['meet','1231','aba','mnm','xx']
z=[x for x in ls if(len(x)>=2 and x[-1]==x[0])]
print(z)


# def myfunc(n):
#     for i in ls:
#         if (len(i)>=2) and (i[-1]==i[0]):
#             print(i)
# myfunc(ls)


