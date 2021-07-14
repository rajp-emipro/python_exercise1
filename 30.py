# Define a dictionary, which is having keys as subject name such as maths, sci etc.
# and marks as values. Sum all the marks. and print the total.

dict = {'maths': 99, 'science': 90, 'physics': 85}
def myfunc(dict):
    total = 0
    for j in dict.values():
        total += j
    return f" the sum of marks is {total}"
print(myfunc(dict))

# using shorter method
dict = {'maths': 99, 'science': 90, 'physics': 85}
print(sum(dict.values()))