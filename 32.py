# Write a Python program to match key values in two dictionaries.
# Sample dictionary: {'key1': 1, 'key2': 3, 'key3': 2}, {'key1': 1, 'key2': 2}
# Expected output: key1: 1 is present in both x and y

x={
    'key1':1,
    'key2':3,
    'key3':2
}
y={
    'key1':1,
    'key2':2
}
# for x_key,x_value in x.items():
#     for y_key,y_value in y.items():
#         if (x_key==y_key)and (x_value==y_value):
#             print(f"{x_key}:{x_value} is present in both x and y")


for k, v in x.items():
    if (k in y) and (x[k] == y[k]):
        print(f"{k}:{x[k]} is present in both x and y")