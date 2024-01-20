"""
    This program demonstrates different formats of while loop
"""

a = 10

# While loop
print('***************** while loop')
while a <= 20:
    print(a)
    a += 2

# Single statement while loop
print('****************** inline while statement')
count = 0
while(count < 5):count += 1; print(f'count: {count}'); print('test')

print('***************** while-else loop')
a = 10
while a <= 20:
    print(a)
    a += 2
else:
    print('while-else block.')
    print(f'Exit value of a: {a}')


# while loop break if a > 18
print('***************** while-else loop with break')
a = 10
while a <= 20:
    if a >= 18:
        break
    print(a)
    a += 2
else:
    print('while-else block.')
    print(f'Exit value of a: {a}')

#
# Output
# --------------
# /usr/bin/python3 /home/viveksingh/wrkspace/python-basics-examples/11-iterations-loops/while_loop.py
# ***************** while loop
# 10
# 12
# 14
# 16
# 18
# 20
# ****************** inline while statement
# count: 1
# test
# count: 2
# test
# count: 3
# test
# count: 4
# test
# count: 5
# test
# ***************** while-else loop
# 10
# 12
# 14
# 16
# 18
# 20
# while-else block.
# Exit value of a: 22
# ***************** while-else loop with break
# 10
# 12
# 14
# 16
#
#
