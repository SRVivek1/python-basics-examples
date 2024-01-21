"""
    This program demonstrates how to iterate and check elements in list
"""


def search_list(list_data, key):
    """
    Print True if key found in the list.
    :param list_data:
    :param key:
    :return:
    """
    r = False
    for i in list_data:
        if i == key:
            r = True

    if r:
        print(f'{skey} found.')
    else:
        print(f'{skey} not found.')


# Driver
if __name__ == '__main__':
    my_list = list([1, 3, 5, 6, 8, 9])

    skey = 81
    search_list(my_list, skey)

    skey = 6
    search_list(my_list, skey)

#
# Output
# -------------
# /usr/bin/python3 /home/viveksingh/wrkspace/python-basics-examples/zz-practice-programs/list_search_element_for_loop.py
# 81 not found.
# 6 found.
#
