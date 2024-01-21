"""
    This class demonstrates single level inheritance in python
"""


class Person:
    """
    Person class.
    """

    def __init__(self, id, name):
        """
        Create a new object with id and name properties.
        :param id:
        :param name:
        """
        self.id = id
        self.name = name

    def display(self):
        """
        Print Person info.
        :return:
        """
        print(f'Id : {self.id}, Name: {self.name}')


class Employee(Person):
    """
    Class Employee inherits Person class.
    """

    def __init__(self, id, name, designation, salary):
        """

        :param id:
        :param name:
        :param designation:
        :param salary:
        """
        # invoking parent constructor
        super().__init__(id, name)

        self.designation = designation
        self.salary = salary

    def details(self):
        print(f'ID : {self.id}')
        print(f'Name : {self.name}')
        print(f'Designation : {self.designation}')
        print(f'Salary : {self.salary}')


# Driver program
obj1 = Employee(1001, 'Vivek', 'Manager', 200000)
print('************** obj1.display()')
obj1.display()

print('************** obj1.details()')
obj1.details()

#
