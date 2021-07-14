# Write a Python program to clone or copy a list.

l1=[1,2,3,4,5]
l2=[]
l2.extend(l1)
print(l2)
l1=[1,2,3,4,5,6]
print(f"change in l1 after extend method {l1}")
print(f"change in l2 after extend method {l2}")



# after using copy method if we change in list1 would list2 be affected or not

l1=[1,2,3,4,5]
l2.copy()
print(l2)
l1=[1,2,3,4,5,6]
print(f"change in l1 after copy method {l1}")
print(f"change in l2 after copy method {l2}")
