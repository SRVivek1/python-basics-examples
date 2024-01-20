"""
    This program demonstrates the use of loop controls - break, continue & pass
"""


# break
# loop from 1 to 100
# break when reaches 30
print('**************************** break')
i = 1
res = list()
while i <= 100:
    # break if i > 30
    if i > 30:
        break
    res.append(i)
    i += 4

print(f"Result list : {res}")


# Continue
# List all divisible by 5
print('**************************** continue')
res = list()
ignore = list()
i = 1
while i <= 100:
    if i % 5 != 0:
        ignore.append(i)
        i += 1
        continue
    res.append(i)
    i += 1

print(f'Divisible by 5 : {res}')
print(f'Ignored : {ignore}')

# Pass
print('**************************** pass')
res, ignore = list(), list()
i = 1
while i <= 10:
    if i % 2 == 0:
        ignore.append(i)
        i += 1
        pass
    res.append(i)
    i += 1

print(f'Not divisible by 2 {res}')
print(f'Ignored : {ignore}')

#
# Output
# ------------------
# /usr/bin/python3 /home/viveksingh/wrkspace/python-basics-examples/11-iterations-loops/loop-controls.py
# **************************** break
# Result list : [1, 5, 9, 13, 17, 21, 25, 29]
# **************************** continue
# Divisible by 5 : [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
# Ignored : [1, 2, 3, 4, 6, 7, 8, 9, 11, 12, 13, 14, 16, 17, 18, 19, 21, 22, 23, 24, 26, 27, 28, 29, 31, 32, 33, 34, 36, 37, 38, 39, 41, 42, 43, 44, 46, 47, 48, 49, 51, 52, 53, 54, 56, 57, 58, 59, 61, 62, 63, 64, 66, 67, 68, 69, 71, 72, 73, 74, 76, 77, 78, 79, 81, 82, 83, 84, 86, 87, 88, 89, 91, 92, 93, 94, 96, 97, 98, 99]
# **************************** pass
# Not divisible by 2 [1, 3, 5, 7, 9, 11]
# Ignored : [2, 4, 6, 8, 10]
#
