"""
    THis class demonstrates the use of @singledispatch decorator.
"""

from functools import singledispatch


@singledispatch
def add_func(args):
    print('add function with args')


@add_func.register(int)
def _(agrs):
    print(f'Int agrs: {agrs}')


@add_func.register(str)
def _(agrs):
    print(f'str agrs: {agrs}')


# Driver
add_func(10)
add_func('hello-world')