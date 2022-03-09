import json

class Employee:
    """
    A class used to represent an Employee

    Attributes
    ----------
    name : str
        A string to represent an employees name
    wage : float
        The hourly pay of an employee
    position : str
        The position an employee holds

    Methods
    -------
    __init__(self, name = None, wage = None, position = None, employee = None)
        default, parametrized, and copy constructor.\n 
        takes in nothing for default constructor.\n 
        takes in name, wage, and position for a parametrized constructor.\n
        takes in an employee class to make a copy of itself.

    setName(self, name)
        sets the name of employee
    
    getName(self):
        gets the name of an employee
    
    setWage(self, wage):
        sets the wage of an employee

    getWage(self):
        gets the wage of an employee

    setPosition(self, pos):
        sets the work postion of an employee

    getPosition(self):
        gets the work postion of an employee

    __repr__(self)
        prints the class in a viewable format
    """

    __name = None
    __wage = None
    __position = None

    def __init__(
        self, name = None, wage = None, position = None, employee = None):
        
        """
        default, parametrized, and copy constructor.\n 
        takes in nothing for default constructor.\n 
        takes in name, wage, and position for a parametrized constructor.\n
        takes in an employee class to make a copy of itself.
        
        Parameters
        ----------
        name : str, optional
            The name of the employee
        wage : float, optional
            The wage of an employee
        position : str, optional
            The work position of an employee
        position : Employee, optional
            The employee that you want to copy
        """

        if name != None:
            self.__name = name
        else:
            self.__name = ''
            
        if wage != None:
            self.__wage = wage
        else:
            self.__wage = 0.0

        if position != None:
            self.__position = position
        else:
            self.__position = ''

        if employee != None:
            self.__name = employee.getName()
            self.__wage = employee.getWage()
            self.__position = employee.getPosition()

    def setName(self, name):
        """
        changes the name of an employee

        Parameters
        ----------
        name : str, optional
            The name of the employee
        """

        self.__name = name
    
    def getName(self):
        """
        returns the name of an employee
        """

        return self.__name
    
    def setWage(self, wage):
        """
        changes the wage of an employee

        Parameters
        ----------
        wage : float, optional
            The wage of the employee
        """

        self.__wage = wage

    def getWage(self):
        """
        returns the wage of an employee
        """

        return self.__wage

    def setPosition(self, pos):
        """
        changes the work position of an employee

        Parameters
        ----------
        name : str, optional
            The work position of the employee
        """

        self.__position = pos

    def getPosition(self):
        """
        returns the work position of an employee
        """

        return self.__position

    def __repr__(self):
        """
        returns the class in a printable fashion
        """
        res = {
            'Name': self.__name,
            'Wage': self.__wage,
            'Position': self.__position
        }

        #makes dictionary print pretty
        res = json.dumps(res, indent=4)

        return res

#               used for testing by runing only this script
#------------------------------------------------------------------------------
# if __name__ == '__main__':
#     bob = Employee('Bob', 12.50, 'Chef')

#     bob2 = Employee(employee = bob)

#     christa = Employee()

#     christa.setName('Christa')
#     christa.setPosition('Manager')
#     christa.setWage(20.25)

#     print(christa.getName(), christa.getWage(), christa.getPosition())
#     print(bob2)
#------------------------------------------------------------------------------