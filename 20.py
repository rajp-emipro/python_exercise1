# Define a global dictionary. Iterate through that dictionary
# and print the output in  the following format.
#
# Sample Output
# a -- 2
# x -- 8
# z -- 1

dict={'a':2,'b':3,'x':8,'z':1}
for key,value in dict.items():
    print(f"{key} -- {value}")

