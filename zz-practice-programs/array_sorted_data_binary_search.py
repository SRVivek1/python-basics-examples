"""
    This program demonstrates the use of binary search on list data.
"""


def binary_search(data, left, right, k):
    while right >= left:

        mid = left + (right - left)//2
        if data[mid] == k:
            return mid

        if data[mid] > k:
            '''search left sub array'''
            return binary_search(data, left, mid - 1, k)

        else:
            '''Search right sub array'''
            return binary_search(data, mid + 1, right, k)

    '''Return -1 as index if data not found'''
    return -1


def search(data, skey):
    low, high = 0, len(data) - 1
    return binary_search(data, low, high, skey)


# Driver program
if __name__ == '__main__':
    arr = [3, 5, 7, 9, 10, 90, 100, 130, 140, 160, 170]

    key = 10
    index = search(arr, key)
    print(f"{key} index: {index}")

    key = 170
    index = search(arr, key)
    print(f"{key} index: {index}")

    key = 105
    index = search(arr, key)
    print(f"{key} index: {index}")

    key = 0
    index = search(arr, key)
    print(f"{key} index: {index}")

    key = 130
    index = search(arr, key)
    print(f"{key} index: {index}")

#
# Output
# -----------------
# /usr/bin/python3 /home/viveksingh/wrkspace/python-basics-examples/zz-practice-programs/array_sorted_data_binary_search.py
# 10 index: 4
# 170 index: 10
# 105 index: -1
# 0 index: -1
# 130 index: 7
#
#

