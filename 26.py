# Define a global dictionary. Define a function which takes 2 values
# 1st as key and 2nd as value. The function should add those key values to the global dictionary.

class Myfunc(dict):
    def add(self,key,value):
        self[key]=value
d=Myfunc()
d.key = input("enter the key:")
d.value = input("enter the value:")
d.add(d.key,d.value)
print(d)
