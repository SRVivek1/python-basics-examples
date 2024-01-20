"""
    This program demonstrates the use of iter() and next() APIs.
"""

# custom list
num_list = [4, 7, 1, 9, 5]

# Create iterator
iterator = iter(num_list)

# print 1st element
print(next(iterator))

# print 2nd element
print(next(iterator))

# use __next__()
print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())

# another next call with throw StopIteration
print(next(iterator))

#
# Output
# ---------------------
# /usr/bin/python3 /home/viveksingh/wrkspace/python-basics-examples/11-iterations-loops/iterator_iter_next_api.py
# 4
# 7
# 1
# 9
# 5
# Traceback (most recent call last):
#   File "/home/viveksingh/wrkspace/python-basics-examples/11-iterations-loops/iterator_iter_next_api.py", line 23, in <module>
#     print(next(iterator))
# StopIteration
#
#
#
