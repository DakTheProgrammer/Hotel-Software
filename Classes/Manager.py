from Employee import Employee
import json

class Manager(Employee):
    """
    A class used to represent a Manager who is an Employee

    Attributes
    ----------
    employeeList : list
        A list of all employees a manager oversees

    Methods
    -------
    __init__(self, name = None, wage = None, employeeList = [], manager = None)
        default, parametrized, and copy constructor.\n 
        takes in nothing for default constructor.\n 
        takes in name, wage, and employeeList for a parametrized constructor.\n
        takes in a Manager class to make a copy of itself.

    setEmployeeList(self, eList)
        sets the Managers list of employees

    def getEmployeeList(self)
        gets the list of employees a manager oversees

    def createEmployee(self, name, wage, position)
        creates a new employee and puts them in there managing list

    def __addEmployee(self, employee)
        privately adds the employee

    def __repr__(self)
        prints the class in a viewable format
    """
    __employeeList = None

    def __init__(
        self, name = None, wage = None, employeeList = [], manager = None):
        """
        default, parametrized, and copy constructor.\n 
        takes in nothing for default constructor.\n 
        takes in name, wage, and employeeList for a parametrized constructor.\n
        takes in a Manager class to make a copy of itself.
        
        Parameters
        ----------
        name : str, optional
            The name of the employee
        wage : float, optional
            The wage of an employee
        employeeList : list, optional
            The list of employees a manager manages
        manager : Manager, optional
            The manager that you want to copy
        """

        if not isinstance(employeeList, list):
            raise TypeError('"employeeList" must be of type list')

        if manager != None:
            super().__init__(manager.getName(), manager.getWage(),
             manager.getPosition())

            self.__employeeList = manager.getEmployeeList()
        else:
            super().__init__(name, wage, 'Manager')

            self.__employeeList = employeeList
            
    def setEmployeeList(self, eList):
        """
        changes the list of employees a manager has

        Parameters
        ----------
        eList : list, optional
            The list of employees
        """
        if not isinstance(eList, list):
            raise TypeError('"employeeList" must be of type list')
        else:
            self.__employeeList = eList

    def getEmployeeList(self):
        """
        gets the list of who a manager manages
        """
        #have to make sure its a list or returns reference
        return list(self.__employeeList)

    def createEmployee(self, name, wage, position):
        """
        creates a new employee

        Parameters
        ----------
        name : str
            name of new employee
        wage : str
            wage of new employee
        position : str
            position of new employee
        """
        self.__addEmployee(Employee(name, wage, position))

    def __addEmployee(self, employee):
        """
        adds new employee to list of employees

        Parameters
        ----------
        employee : Employee
            new employee
        """
        self.__employeeList.append(employee)

    def __repr__(self):
        """
        returns the class in a printable fashion
        """

        elist = []

        for emps in self.__employeeList:
            elist.append(json.loads(emps.__repr__()))

        res = {
            'Name': self.getName(),
            'Wage': self.getWage(),
            'Position': self.getPosition(),
            'Managing': elist
        }

        #makes dictionary print pretty
        res = json.dumps(res, indent=4)

        return res
        
#               used for testing by runing only this script
#------------------------------------------------------------------------------
# if __name__ == '__main__':
#     pat = Employee('Pat', 7.25, 'House Keeper')
#     jim = Employee('Jim', 10.5, 'Chef')
#     jan = Employee('Jan', 15, 'Desk Worker')

#     bill = Manager('bill', 25.75, [pat, jim, jan])
#     bill2 = Manager(manager = bill)

#     #abe is only managed by bill2
#     bill2.createEmployee('abe', 7.25, 'Bellhop') 

#     print(bill2)
#------------------------------------------------------------------------------