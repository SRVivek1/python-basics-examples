"""
    Hellow world app, with functions
"""


def greet(name):
    """
    Say Hi to the person with given name.
    :param name:
    :return:
    """
    print(f'Hello Mr. {name}')


def is_even(num):
    """
    Print True if it's even number.
    :param num:
    :return:
    """
    print(num % 2 == 0)


if __name__ == "__main__":
    """
    This is the syntax of main method.
    """

    print('Inside main method.')

    # Greet
    greet('Mohit')
    print(f'is_even(23) : {is_even(23)}')

#
# Output
# -------------
# /usr/bin/python3 /home/viveksingh/wrkspace/python-basics-examples/01-hello-world/hello-world.py
# Inside main method.
# Hello Mr. Mohit
# False
# is_even(23) : None
#
#
