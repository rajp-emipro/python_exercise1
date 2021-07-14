# Define a global empty dictionary. Iterate from 1 till 10 and
# fill the dictionary with the key as the number and value as the square of that number.
d={}
print(d)
d={value:value*value for value in range(1,11)}
print(d)
