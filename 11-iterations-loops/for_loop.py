"""
    This program demonstrates for loop.
"""

print("********************************** String chars ")
name = 'helloindia'
for char in name:
    print(char, end=', ')
print(end='\n')


# Printing List
print("********************************** List ")
num_list = [i for i in range(1, 41, 6)]
print(f'Num List : {num_list}')

# print all elements of list
print('Printing list data: ')
for num in num_list:
    print(num, end=', ')

print(end='\n')


print("********************************** Tuple ")
fruits = ('apple', 'orange', 'banana', 'guava')
for fruit in fruits:
    print(f'{fruit} : {len(fruit)}', end=', ')

print(end='\n')


print("********************************** dict ")
temp = dict()
temp['a'] = 65
temp['b'] = 66
temp['c'] = 67

for t in temp:
    print(t, temp[t])

#
# Output
# -------------------
# /usr/bin/python3 /home/viveksingh/wrkspace/python-basics-examples/11-iterations-loops/for_loop.py
# ********************************** String chars
# h, e, l, l, o, i, n, d, i, a,
# ********************************** List
# Num List : [1, 7, 13, 19, 25, 31, 37]
# Printing list data:
# 1, 7, 13, 19, 25, 31, 37,
# ********************************** Tuple
# apple : 5, orange : 6, banana : 6, guava : 5,
# ********************************** dict
# a 65
# b 66
# c 67
#
