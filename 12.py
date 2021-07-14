# Write a Python program to remove the first item from a specified list.
color = ["Red", "Black", "Green", "White", "Orange"]
num = [255,3678,95,158,759,157]
#
x=color.pop(0)
print(f"the removed element is {x}")
print(color)


y=num.pop(0)
print(f"the removed element is {y}")
print(num)

color = ["Red", "Black", "Green", "White", "Orange"]
for i in color:
    print(i)
    color.pop('i')
color[:] = []
print(color)


num = [255,3678,95,158,759,157]
for i in num:
    print(i)
    num.pop('i')
