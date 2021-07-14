# d = {7: 2, 9: 4, 4: 3, 2: 1, 0: 0} Sort this dictionary ascending and descending.



# print(help(sorted(d1)))
d1 = {7: 2, 9: 4, 4: 3, 2: 1, 0: 0}
d2=dict(sorted(d1.items(),key=lambda item:item[1]))
print(d2)
d3=dict(sorted(d1.items(), key=lambda item: item[1],reverse=True))
print(d3)

