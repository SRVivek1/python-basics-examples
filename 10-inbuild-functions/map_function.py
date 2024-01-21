"""
    This program demonstrates the
"""

list_1 = list([1, 3, 5, 7, 9, 11])
list_2 = [2, 4, 6, 8, 10, 12]
list_3 = ['a', 'b', 'c']
list_4 = ['d', 'e', 'f']

print('******************* add list elements index wise - res = list(map(lambda a, b: a + b, list_1, list_2))')
res = list(map(lambda a, b: a + b, list_1, list_2))
print(f'Result type : {type(res)}')
print(f'Result list : {res}')


print('***************** Add list with heterogeneous content')
res = list(map(lambda a, b: a + '-' + b, list_3, list_4))
print(f'Result type : {type(res)}')
print(f'Result list : {res}')

#
# Output
# ----------------
# /usr/bin/python3 /home/viveksingh/wrkspace/python-basics-examples/10-inbuild-functions/map_function.py
# ******************* add list elements index wise - res = list(map(lambda a, b: a + b, list_1, list_2))
# Result type : <class 'list'>
# Result list : [3, 7, 11, 15, 19, 23]
# ***************** Add list with heterogeneous content
# Result type : <class 'list'>
# Result list : ['a-d', 'b-e', 'c-f']
#
#
#
