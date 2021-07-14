# Create a function which takes a value. Define a global dictionary.
# The function should be able to display a statement whether the passed value is in the dictionary or not.

def myfunc(n):
    dict={'name':'meet','age':'22','subject':'python'}
    if n in dict.values():
        print("yes  the word you searched is there in dictionary")
    else:
        print("sorry the word is'nt present in the dictionary")
val=input("enter value want to search in dictionary:")
myfunc(val)
