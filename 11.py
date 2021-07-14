# Define a global dictionary. Iterate through it and print the key and value of it separately
# in the following format.
# Key is <key> and Value is <value>

dict={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
for i,j in dict.items():
    print(f"The key is {i} and value is {j}")