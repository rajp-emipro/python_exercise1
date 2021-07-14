# write a program which accepts a sequence of comma-seperated values from user and
# generate list and tuple with those numbers
# a.sampledata:3,5,7,23
# b.output:1,
# list=['3','5','7','23']
# tuple=('3','5','7','23')

number=input("enter number you want seperated by comma(,):").split(',')
print(number)
print(type(number))
tup=tuple(number)
print(tup)
print(type(tup))
