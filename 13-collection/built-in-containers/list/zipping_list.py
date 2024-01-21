"""
    This program demonstrates how to merge two lists to get tuple of elements from both lists.
"""

emp = ['Vivek', 'India', 'Nokia']
titles = ['Name', 'loc', 'Company']

zipped = zip(emp, titles)

print(type(zipped))
print(zipped)

for e in zipped:
    print(e)

# Output
# --------------
# /usr/bin/python3 /home/viveksingh/wrkspace/python-basics-examples/13-collection/mergin_list.py
# <class 'zip'>
# <zip object at 0x75057aa904c0>
# ('Vivek', 'Name')
# ('India', 'loc')
# ('Nokia', 'Company')
#
