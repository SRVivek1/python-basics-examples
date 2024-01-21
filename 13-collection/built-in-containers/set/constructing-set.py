"""
    This program demonstrates various ways to create set instance.
"""


# {} - creates an empty dict not a set.
sett = {}
print(f"type(sett) : {type(sett)}")

# Homogeneous objects
sett = {1, 2, 3, 5}
print(f"type(sett) : {type(sett)}")


# Heterogeneous objects
sett = {1001, 'vivek', 'India'}
print(f"type(sett) : {type(sett)}")


# str data
sett = {"HelloWorld"}
print(f"type(sett) : {type(sett)}")
print(f'str data : {sett}')


# can be use to type cast other collection
# if no args passed create empty set
sett = set()
print(f"type(sett) : {type(sett)}")

# str data is converted into char
sett = set("HelloWorld")
print(f"type(sett) : {type(sett)}")
print(f'str data : {sett}')

# List to set
my_list = [1, 5, 10, 15, 20]
print(f'type(my_list): {type(my_list)}')
sett = set(my_list)
print(f"type(sett) : {type(sett)}")
print(f'list data : {sett}')

#
# Output
# --------------
# /usr/bin/python3 /home/viveksingh/wrkspace/python-basics-examples/13-collection/built-in-containers/set/constructing-set.py
# type(sett) : <class 'dict'>
# type(sett) : <class 'set'>
# type(sett) : <class 'set'>
# type(sett) : <class 'set'>
# str data : {'HelloWorld'}
# type(sett) : <class 'set'>
# type(sett) : <class 'set'>
# str data : {'r', 'l', 'W', 'o', 'd', 'H', 'e'}
# type(my_list): <class 'list'>
# type(sett) : <class 'set'>
# list data : {1, 5, 10, 15, 20}
#
