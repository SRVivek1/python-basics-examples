"""
    This program demonstrates the function - ininstance()
"""


def is_supported(param):
    """
    Using isinstance() function check the type of parameter.
    :param param:
    :return:
    """
    if isinstance(param, int):
        print('int type')
    elif isinstance(param, str):
        print('str type')
    else:
        print('Unsupported type')


empId = 1001
name = 'Rohit'
salary = 200000.00

print(f'is_supported(empId)')
is_supported(empId)

print(f'is_supported(name)')
is_supported(name)

print(f'is_supported(salary)')
is_supported(salary)

#
# Output
# ---------------
# /usr/bin/python3 /home/viveksingh/wrkspace/python-basics-examples/10-inbuild-methods/a1-is-instance.py
# is_supported(empId)
# int type
# is_supported(name)
# str type
# is_supported(salary)
# Unsupported type
#
