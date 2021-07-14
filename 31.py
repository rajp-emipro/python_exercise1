# students = {'Aex':{'class':'V', 'roll_id':2}, 'Puja':{'class':'V',’roll_id':3}}
# Using the above dictionary, print the following output.
# 1}Aex
# 2}class : V
# 3}roll_id : 2
# 4}Puja
# 5}class : V
# 6}roll_id : 3

students = {'Aex':
                {'class':'V',
                 'roll_id':2
                 },
            'Puja':
                {'class':'V',
                 'roll_id':3
                 }
            }

# x=list(students.keys())[0]
# print(x)
# #
# for name,info in students.items():
#     print(name)
#     for key in info:
#         print(f"{key}:{info[key]}")
#

# we can use items instead of info in 2nd loop or not
# according to below mentioned solution?

for name,info in students.items():
    print(name)
    for i,j in info.items():
        print(f"{i}:{j}")




