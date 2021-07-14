# Define a global dictionary. Iterate through it
# and print the key and value of it separately in the following format.
# Key is <key> and Value is <value>.
# The loop statement should be enough to extract key and value,
# so don't use the "get" method or [] to extract the value from the dictionary.


dict1={'name':'Meet','age':22,'lastname':'Dhruv'}
for i,j in dict1.items():
    print(f"key is {i} \n and value is {j}")