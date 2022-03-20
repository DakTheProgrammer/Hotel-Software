from Employee import Employee
from Guest import Guest
from Room import Room
import json

class Attendant(Employee):
    """
    A class used to represent an Attendant who is an Employee

    Attributes
    ----------
    employeeList : list
        A list of all employees within hotel
    roomList    :   list
        A list of all rooms within the hotel

    Methods
    -------
    __init__(self, name = None, wage = None, employeeList = [], roomList = [], attendant = None)
        default, parametrized, and copy constructor.\n 
        takes in nothing for default constructor.\n 
        takes in name, wage, employeeList, and roomList for a parametrized constructor.\n
        takes in a Attendant class to make a copy of itself.

    def checkInGuest(self, guest)
        checks a guest into a hotel room

    def checkOutGuest(self, guest)
        checks a guest out of the hotel

    def getEmployeeList(self)
        gets the list of employees within the hotel

    def getRoomList(self)
        gets the list of rooms within the hotel

    def __repr__(self)
        prints the class in a viewable format
    """
    __employeeList = None
    __roomList = None

    def __init__(
        self, name = None, wage = None, employeeList = [], roomList = [], attendant = None):
        """
        default, parametrized, and copy constructor.\n 
        takes in nothing for default constructor.\n 
        takes in name, wage, employeeList, and roomList for a parametrized constructor.\n
        takes in a Attendant class to make a copy of itself.
        
        Parameters
        ----------
        name : str, optional
            The name of the employee
        wage : float, optional
            The wage of an employee
        employeeList : list, optional
            The list of employees currently working
        roomList : list, optional
            The list of rooms within the hotel
        attendant : Attendant, optional
            The attendant that you want to copy
        """

        if not isinstance(employeeList, list):
            raise TypeError('"employeeList" must be of type list')
        
        if not isinstance(roomList, list):
            raise TypeError('"roomList" must be of type list')

        if attendant != None:
            super().__init__(attendant.getName(), attendant.getWage(),
             attendant.getPosition())

            self.__employeeList = attendant.getEmployeeList()
            self.__roomList = attendant.getRoomList()
        else:
            super().__init__(name, wage, 'Attendant')

            self.__employeeList = employeeList
            self.__roomList = roomList
            
    def checkInGuest(self, guest):
        """
        checks a guest into a hotel room that is available

        Parameters
        ----------
        guest : Guest, optional
            the guest to be checked into a room
        """
        if not isinstance(guest, Guest):
            raise TypeError('"guest" must be of type Guest')

        else:        #Find a room that is clean and unoccupied
            for room in self.__roomList:
                if room.getStatus() == "clean":
                    guest.setRoom(room)
                    break

    def checkOutGuest(self, guest):
        """
        checks a guest out of the hotel room

        Parameters
        ----------
        guest : Guest, optional
            the guest to be checked out of a room
        """
        if not isinstance(guest, Guest):
            raise TypeError('"guest" must be of type Guest')

        else:   #Remove room from guest account and lable room as dirty
            room = guest.getRoom()
            room.setStatus("dirty")
            guest.setRoom(None)

    def getEmployeeList(self):
        """
        gets the list of employees currently working
        """
        return list(self.__employeeList)

    def getRoomList(self):
        """
        gets the list of rooms within the hotel
        """
        return list(self.__roomList)

    def __repr__(self):
        """
        returns the class in a printable fashion
        """

        rlist = []

        for rooms in self.__roomList:
            rlist.append(rooms.__repr__().split('\n'))

        res = {
            'Name': self.getName(),
            'Wage': self.getWage(),
            'Position': self.getPosition(),
            'Rooms Attending' : rlist
        }

        res = json.dumps(res, indent=4)

        return res
        
#------------------------------------------------------------------------------
# if __name__ == '__main__':
#     joe = Employee('Joe', 7.50, 'House Keeper')
#     john = Employee('John', 11.5, 'Chef')

#     rm114 = Room(114, 'Standard', 2, 'dirty')
#     rm220 = Room(220, 'Suite', 1, 'clean')

#     eddie = Guest(name = 'Eddie', balance = 140, hotelInfo=['Pool: 10:00-5:00', 'Gym: 3:00-9:00'])

#     sal = Attendant('Sal', 15.75, [joe, john], [rm114, rm220])
#     sal2 = Attendant(attendant = sal)

#     sal.checkInGuest(eddie)

#     print(sal)
#     print('--------------')
#     print(eddie)

#     sal.checkOutGuest(eddie)
#------------------------------------------------------------------------------