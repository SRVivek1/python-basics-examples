"""
    THis program demonstrates custom iterator.
"""

# TODO - CHECK PAGE 68

class PowTwo:
    """
    Custom Iterator class, it take int value and return it\'s pow of 2.
    """
    def __init__(self, max = 0):
        """
        Initialize max property till which the pow of 2 value can be calculated.
        :param max:
        """
        self.max = max

    def __iter__(self):
        """
        Initialize property from where to start n = 0.
        Return self instance.
        :return:
        """
        self.n = 0
        return self

    def __next__(self):
        """
        Calculates pow from n to max.
        :return:
        """
        if self.n > self.max:
            raise StopIteration

        result = 2 ** self.n
        self.n += 1
        return result


# main method
if __name__ == '__main__':
    """
    Driver program.
    """
    obj = PowTwo(4)
    obj_iter = iter(obj)

    # print next values
    print(next(obj_iter))
    print(next(obj_iter))
    print(next(obj_iter))
    print(next(obj_iter))
    print(next(obj_iter))
    print(next(obj_iter))

#
# Output
# -------------------
# /usr/bin/python3 /home/viveksingh/wrkspace/python-basics-examples/11-iterations-loops/custom_iterator.py
# 1
# 2
# 4
# 8
# 16
# Traceback (most recent call last):
#   File "/home/viveksingh/wrkspace/python-basics-examples/11-iterations-loops/custom_iterator.py", line 54, in <module>
#     print(next(obj_iter))
#   File "/home/viveksingh/wrkspace/python-basics-examples/11-iterations-loops/custom_iterator.py", line 33, in __next__
#     raise StopIteration
# StopIteration
#
