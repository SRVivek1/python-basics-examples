"""
    THis program is to find the first repeating element in an array.
"""


def find_first_repeating_element_index(arr):
    """
    Return the index of first repeating element.
    :param arr:
    :return:
    """
    element_dict = dict()

    for i, e in enumerate(arr):
        if element_dict.get(e) is not None:
            return element_dict.get(e)

        # add to dict
        element_dict[e] = i


# Driver program
if __name__ == '__main__':
    arr = [2, 4, 5, 7, 4, 5, 9, 11, 15]
    index = find_first_repeating_element_index(arr)
    print(f'Index : {index}')

    arr = [2, 4, 5, 7, 9, 11, 15, 9]
    index = find_first_repeating_element_index(arr)
    print(f'Index : {index}')

    arr = [2, 4, 5, 7, 9, 11, 15, 0, 15]
    index = find_first_repeating_element_index(arr)
    print(f'Index : {index}')

#
# Output
# ---------------------------
# /usr/bin/python3 /home/viveksingh/wrkspace/python-basics-examples/zz-practice-programs/array_find_first_repeating_element.py
# Index : 1
# Index : 4
# Index : 6
#
#
# #