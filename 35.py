# Write a Python program to filter the height and width of students,
# which are stored in a dictionary. Height >= 6ft and Weight>= 70kg:
#
# a}Original Dictionary: {'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}
#
# b}Output : {'Cierra Vega': (6.2, 70)}


# students= {'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}
#
# def myfunc(students):
#     for i,j in students.items():
#         if j[0]>=6.0 and j[1]>=70:
#             print(f"{i}:{j}")
# myfunc(students)


# using dictinary comprehension

dic = {'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}
# x={key:value for key,value in dic.items() if value[0]>=6.0 and value[1]>=70}
# print(x)


# number_list = range(-5, 5)
# less_than_zero = list(filter(lambda x: x < 0, number_list))
# print(less_than_zero)



# using lambda filter function

students= {'Cierra Vega': (6.2, 70),'Cia': (6.8, 76), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}
x= dict(filter(lambda x:(x[1][0]>(5.9)) and (x[1][1] >=(70.0)),students.items()))
print(x)





# =========================================================================================
# # filter with lambda
# fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
# filter_object = filter(lambda s: s[0] == "A", fruit)
# print(list(filter_object))
#
# # filter without lambda
# def starts_with_A(s):
#     return s[0] == "A"
# fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
# filter_object = filter(starts_with_A, fruit)
# print(list(filter_object))
#
#
#

