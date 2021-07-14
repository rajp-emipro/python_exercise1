# Write a Python program to drop empty(None) Items from a given Dictionary.
# a}Original Dictionary - {'c1': 'Red', 'c2': 'Green', 'c3': None}
# b}New Dictionary after dropping empty items: {'c1': 'Red', 'c2': 'Green'}


d={'c1': 'Red', 'c2': 'Green', 'c3': None}
print(d)
d= {key:value for (key, value) in d.items() if value!=None}
print(d)