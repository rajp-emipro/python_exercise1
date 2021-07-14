# Take 3 global dictionaries as follows. Define a function, which takes those 3 dictionaries
# and concatenate them.
#
#
# a)dic1={1:10, 2:20}
# b)dic2={3:30, 4:40}
# c)dic3={5:50,6:60}
# d)Output should be - {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}


# dict1={1:10, 2:20}
# dict2={3:30, 4:40}
# dict3={5:50,6:60}
# dict4 = {**dict1,**dict2,**dict3}
# print(dict4)

dict1 = {1: 10, 2:20}
dict2={3:30, 4:40,2:40}
dict3={5:50,6:60}
dict4 = {**dict1,**dict2,**dict3}
print(dict4)
