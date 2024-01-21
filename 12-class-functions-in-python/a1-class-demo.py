"""
    This class demonstrates a sample class structure.
"""


class Dog:
    """
    Dog class.
    """

    '''Class attribute'''
    type = 'mammal'

    def __init__(self, breed):
        """
        Dog constructor.
        """
        '''Instance attribute'''
        self.breed = breed


    def speak(self):
        """
        function of class.
        :return:
        """
        print(f'I am {self.breed} breed.')


# Driver
obj1 = Dog('German')
obj2 = Dog('Husky')

# accessing methods
obj1.speak()
obj2.speak()

# accessing class attributes
print(f'obj1.__class__.type: {obj1.__class__.type}')

#
