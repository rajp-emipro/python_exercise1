# Write a Python program that will accept the base and height of a triangle
# and compute the area.

# 1/2 hb
# method 1
def area(h,b):
    return (1/2)*h*b
print(area(2,3))

    # method2
x=lambda h,b:(0.5)*h*b
print(x(2,3))
