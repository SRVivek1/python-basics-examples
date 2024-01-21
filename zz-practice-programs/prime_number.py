"""
    This program demonstrates the prime number problem.
"""


def is_prime(num) -> bool:
    """
    Returns true if the number is prime.
    :param num:
    :return:
    """
    if num == 1:
        return True

    for i in range(2, int(num / 2) + 1):
        if num % i == 0:
            return False

    return True


# Driver program
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 13, 15, 19, 40, 67]

for a in arr:
    res = is_prime(a)
    if res:
        print(f'{a} - Prime.')
    else:
        print(f'{a} - Not Prime')

#
# Output
# --------------------
# /usr/bin/python3 /home/viveksingh/wrkspace/python-basics-examples/zz-practice-programs/prime_number.py
# 1 - Prime.
# 2 - Prime.
# 3 - Prime.
# 4 - Not Prime
# 5 - Prime.
# 6 - Not Prime
# 7 - Prime.
# 8 - Not Prime
# 9 - Not Prime
# 10 - Not Prime
# 13 - Prime.
# 15 - Not Prime
# 19 - Prime.
# 40 - Not Prime
# 67 - Prime.
#
#
