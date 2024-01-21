"""
    This class demonstrates the class and it's property scope.
"""

class Person:
    """
    Parent class.
    """

    def __init__(self, intro):
        """
        Initialize instances.
        """
        self.intro = intro
        self.__secret = 'RAW Agent'

    def info_internal(self):
        print(f'Intro : {self.intro}, Secret: {self.__secret}')


class Employee(Person):
    """
    Employee is a Person.
    """

    def __init__(self, name, intro):
        """
        :param name:
        :param intro:
        """
        super().__init__(intro)
        self.name = name

    def info(self):
        print(f'Name : {self.name}, Info : {self.intro}')

        # self.__secret - is not visible
        # print(f'Secret : {self.__secret}')
        self.info_internal()


# Driver program
obj1 = Employee('Vivek', 'I\'m learner')
obj1.info()
