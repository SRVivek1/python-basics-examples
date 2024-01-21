"""
 This program demonstrates how to search in an infinite array.
"""


def binary_search(a, l, r, k):
    """
    Find the key in array using search technique.

    :param a:
    :param l:
    :param r:
    :param k:
    :return:
    """
    while r >= l:

        mid = l + (r - l) // 2

        if a[mid] == k:
            return mid

        if a[mid] > k:
            return binary_search(a, l, mid - 1, k)
        else:
            return binary_search(a, mid + 1, r, k)

    return -1


def search(data, key):
    """
    Search for key in an infinite array.
    :param arr:
    :param key:
    :return:
    """

    '''
        find sub array where data exists
        we have left so we'll find right index 
        which is when val becomes greater than key.
    '''
    left, right, val = 0, 1, data[0]
    while val < key:
        left = right
        right = right * 2
        val = data[right]

    '''find using binary search'''
    return binary_search(data, left, right, key)


# Driver program
if __name__ == '__main__':
    arr = [3, 5, 7, 9, 10, 90, 100, 130, 140, 160, 170]

    key = 10
    index = search(arr, key)
    print(f"{key} index: {index}")

    key = 2
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
# /usr/bin/python3 /home/viveksingh/wrkspace/python-basics-examples/zz-practice-programs/array_infinite_sorted_data_binary_search.py
# 10 index: 4
# 2 index: -1
# 105 index: -1
# 0 index: -1
# 130 index: 7
#
#
# #