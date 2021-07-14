# Write a Python program to count the number occurrence of a specific character in a string.
# str="Hello my name is meet.meet is from rajkot.meet knows python"
# x=str.count("meet")
# print(f"the word is repeated {x}times")

# my name is Mmeet

str=input('enter the string or name you want to count letter:')
for i in set(str.replace(' ','').lower()):
    print(f"the letter {i} is repeated {str.count(i)}times")



# str="Hello my name is meet.meet is from rajkot.meet knows python"
# print(f"a is repeated {str.count('a')} times")
# print(f"b is repeated {str.count('b')} times")
# print(f"c is repeated {str.count('c')} times")
# print(f"d is repeated {str.count('d')} times")
# print(f"e is repeated {str.count('e')} times")
# print(f"f is repeated {str.count('f')} times")
# print(f"g is repeated {str.count('g')} times")
# print(f"h is repeated {str.count('h')} times")
# print(f"i is repeated {str.count('i')} times")
# print(f"j is repeated {str.count('j')} times")