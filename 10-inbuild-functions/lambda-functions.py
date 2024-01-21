"""
    This program demonstrates the lambda expression.
"""


print('*********************** str upper : lambda loc: loc.upper()')
# Convert str to upper case
address = 'india'

# lambda func
upper = lambda loc: loc.upper()

print(f'Input - {address}')
print(f'Updated : {upper(address)}')


print('****************** Square : lambda n: n * n')
# For a list of numbers, get their square
nums_list = [i for i in range(1, 6)]

# lambda square function
square_fun = lambda n: n * n

res = list(map(square_fun, nums_list))
print(f'Data : {nums_list}')
print(f'Square : {res}')
