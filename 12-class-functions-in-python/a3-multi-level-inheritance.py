"""
    This class demonstrates multi level inheritance in python
"""


class Human:
    """
    Human class.
    """

    def __init__(self, info):
        """

        :param info:
        """
        self.info = info

    def information(self):
        print(f'Human : {self.info}')


class Person(Human):
    """
    Person class.
    """

    def __init__(self, id, name, info):
        """
        Create a new object with id and name properties.
        :param id:
        :param name:
        """
        # call to Human class constructor
        super().__init__(info)
        self.id = id
        self.name = name

    def display(self):
        """
        Print Person info.
        :return:
        """
        print(f'Id : {self.id}, Name: {self.name}, Info: {self.info}')


class Employee(Person):
    """
    Class Employee inherits Person class.
    """

    def __init__(self, id, name, designation, salary, info):
        """

        :param id:
        :param name:
        :param designation:
        :param salary:
        """
        # invoking parent constructor
        super().__init__(id, name, info)

        self.designation = designation
        self.salary = salary

    def details(self):
        print(f'ID : {self.id}')
        print(f'Name : {self.name}')
        print(f'Designation : {self.designation}')
        print(f'Salary : {self.salary}')
        print(f'Salary : {self.info}')


# Driver program
obj1 = Employee(1001, 'Vivek', 'Manager', 200000, '20th century human being.')

print('************** obj1.info()')
obj1.information()

print('************** obj1.display()')
obj1.display()

print('************** obj1.details()')
obj1.details()

#
