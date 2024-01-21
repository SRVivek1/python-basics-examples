"""
    This program demonstrates the syntax and use of variable length arguments.
    Operator:
        *
            -> Known as unpacking operator.
            -> Reads data as tuple.

        **
            -> Also known as named parameter operator.
            -> Read data as dict.
"""


def positional_args_sum(*nums):
    """
    This method accepts args as tuple
    :param nums:
    :return:
    """
    print(f'Data type : {type(nums)}')
    print(f'Data : {nums}')

    # do business operations as needed on tuple
    counter = 0
    for element in nums:
        if isinstance(element, int):
            counter += element
    print(f'Integer sum : {counter}')


def named_args_func(**input_args):
    """
    This function accepts args as dict
    :param kwargs:
    :return:
    """
    print(f'**kwargs type: {type(input_args)}')
    print(f'**kwargs data: {input_args}')

    # business logic to process dict data type


# Driver program
if __name__ == '__main__':

    # agrs as tuple
    fruits = ('apple', 'mango', 'guava', 'banana')
    vegetables = ('tomato', 'potato', 'cabbage', 'carrot')

    print('****************** Single arg -  positional_args_sum(fruits)')
    positional_args_sum(fruits)

    print('****************** Multiple arg -  positional_args_sum(fruits, vegetables)')
    positional_args_sum(fruits, vegetables)

    print('****************** Multiple int args : positional_args_sum(10, 20, 30, 40) ')
    positional_args_sum(10, 20, 30, 40)

    print("****************** Multiple heterogeneous args : positional_args_sum(10, 20, 30, 40, 'abc', 'xyz')")
    positional_args_sum(10, 20, 30, 40, 50, 'abc', 'xyz')

    # args as dict
    print('******************* **args read as dict *******************************')

    print("Input : named_args_func(first='hello', mid='India', last='Good Morning')")
    named_args_func(first='hello', mid='India', last='Good Morning')

    print("Input : named_args_func(name='Vivek', loc='Bangalore', age=50, mob=524100354)")
    named_args_func(name='Vivek', loc='Bangalore', age=50, mob=524100354)


#
# Output
# ----------------
# /usr/bin/python3 /home/viveksingh/wrkspace/python-basics-examples/12-class-functions-in-python/variable-length-args.py
# ****************** Single arg -  positional_args_sum(fruits)
# Data type : <class 'tuple'>
# Data : (('apple', 'mango', 'guava', 'banana'),)
# Integer sum : 0
# ****************** Multiple arg -  positional_args_sum(fruits, vegetables)
# Data type : <class 'tuple'>
# Data : (('apple', 'mango', 'guava', 'banana'), ('tomato', 'potato', 'cabbage', 'carrot'))
# Integer sum : 0
# ****************** Multiple int args : positional_args_sum(10, 20, 30, 40)
# Data type : <class 'tuple'>
# Data : (10, 20, 30, 40)
# Integer sum : 100
# ****************** Multiple heterogeneous args : positional_args_sum(10, 20, 30, 40, 'abc', 'xyz')
# Data type : <class 'tuple'>
# Data : (10, 20, 30, 40, 50, 'abc', 'xyz')
# Integer sum : 150
# ******************* **args read as dict *******************************
# Input : named_args_func(first='hello', mid='India', last='Good Morning')
# **kwargs type: <class 'dict'>
# **kwargs data: {'first': 'hello', 'mid': 'India', 'last': 'Good Morning'}
# Input : named_args_func(name='Vivek', loc='Bangalore', age=50, mob=524100354)
# **kwargs type: <class 'dict'>
# **kwargs data: {'name': 'Vivek', 'loc': 'Bangalore', 'age': 50, 'mob': 524100354}
#

