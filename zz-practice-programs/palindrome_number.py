"""
    This program take a number and checks if it's palindrome.
"""


def reverse_num(n):
    """
    Returns the reverse of the given number.
    :param n:
    :return:
    """
    rev = 0
    while n > 0:
        t = n % 10
        rev = (rev * 10) + t
        n = int(n / 10)
    return rev


def check_palindrome(rev_func, num):
    """
    Checks if the given number is a palindrome or not.
    :param num:
    :param rev_func:
    :return:
    """
    rev = rev_func(num)
    print(f'Num : {num} \nReverse: {rev}')
    if num == rev:
        print(f'Number {num} is palindrome')
    else:
        print(f'{num} is not a palindrome number')


# Driver
if __name__ == '__main__':
    data = 12421
    check_palindrome(reverse_num, data)

#
# Output
# ---------------------
# /usr/bin/python3 /home/viveksingh/wrkspace/python-basics-examples/zz-practice-programs/palindrome_number.py
# Num : 12421
# Reverse: 12421
# Number 12421 is palindrome
#

