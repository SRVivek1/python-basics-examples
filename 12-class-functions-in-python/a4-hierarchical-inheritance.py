"""
    This class demonstrates Hierarchical inheritance.
    That is a single parent will have multiple child.
"""


class Animal:
    """
    Animal class.
    """

    def __init__(self, habitat):
        """
        Constructor.
        Type - Wild, pet.
        :param habitat:
        """
        self.habitat = habitat


class Dog(Animal):
    """
    Dog is an Animal.
    """

    def __init__(self, habitat, name):
        super().__init__(habitat)
        self.name = name

    def info(self):
        print(f'Dog\'s name {self.name}, it\'s {self.habitat} animal.')


class Lion(Animal):
    """
    Lion is an Animal.
    """

    def __init__(self, habitat, name):
        super().__init__(habitat)
        self.name = name

    def info(self):
        print(f'Lion\'s name {self.name}, it\'s {self.habitat} animal.')


# Driver program
lion1 = Lion('wild', 'Rocky')
dog1 = Dog('pet', 'Puchchu')

print('*************** lion1.info()')
lion1.info()

print('*************** dog1.info()')
dog1.info()

#
# Output
# --------------
# /usr/bin/python3 /home/viveksingh/wrkspace/python-basics-examples/12-class-functions-in-python/a4-hierarchical-inheritance.py
# *************** lion1.info()
# Lion's name Rocky, it's wild animal.
# *************** dog1.info()
# Dog's name Puchchu, it's pet animal.
#

