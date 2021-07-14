# # 8}Write a Python program to test whether a passed letter is a vowel or not
# def vow(n):
#     vowel =['a', 'e', 'i', 'o', 'u']
#     if n in vowel:
#         print("yes it is a vowel letter")
#     else:
#         print('no it isn\'t a vowel')
# str=input('enter a letter you want to check:')
# vow(str)

# my name is meet.i have completed my engineering from atmiya university


string=input("Enter string:")
vowels=0
v=['a','e','i','o','u']
for i in string:
    for j in v:
        if i==j:
            vowels = vowels + 1
print("Number of vowels are:")
print(vowels)


print(f"the vowel a is {string.count('a')} times")
print(f"the vowel e is {string.count('e')} times")
print(f"the vowel i is {string.count('i')} times")
print(f"the vowel o is {string.count('o')} times")
print(f"the vowel u is {string.count('u')} times")

# outside the loop
# extra loop
