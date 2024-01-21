"""
    Merge data from two lists.
"""

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
weekends = ['Saturday', 'Sunday']

# Merge lists
print('******************** days = weekdays.__add__(weekends)')
days = weekdays.__add__(weekends)
print(f'Days : {days}')


print('******************** days = weekdays + weekends')
days = weekdays + weekends
print(f'Days : {days}')

#
# Output
# -------------
# /usr/bin/python3 /home/viveksingh/wrkspace/python-basics-examples/13-collection/merging_two_lists.py
# ******************** days = weekdays.__add__(weekends)
# Days : ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
# ******************** days = weekdays + weekends
# Days : ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
#
