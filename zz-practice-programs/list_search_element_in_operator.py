"""
    This program demonstrates how to iterate and check elements in list
"""


def search_key(data, key):
    # Using in operator
    if key in data:
        print(f'{key} found.')
    else:
        print(f'{key} not found.')


# Driver
if __name__ == '__main__':
    my_list = list([1, 3, 5, 6, 8, 9])

    skey = 8
    search_key(my_list, skey)

    skey = 81
    search_key(my_list, skey)

#
# Output
# ----------------
# /usr/bin/python3 /home/viveksingh/wrkspace/python-basics-examples/zz-practice-programs/list_search_element_in_operator.py
# 8 found.
# 81 not found.
#
#
#
