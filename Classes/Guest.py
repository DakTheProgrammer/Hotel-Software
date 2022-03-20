import json
from Room import Room

class Guest():
    """
    A class used to represent a Guest within the hotel

    Attributes
    ----------
    name : str
        Name of the guest staying at hotel

    room : Room
        Instance containing a guest's room and its contents

    balance  :   float
        Current balance charged to guest to pay
    
    hotelInfo   : HotelInfo
        Information containing all general hotel hours


    Methods
    -------
    __init__(self, room = None, balance = 0, hotelInfo = None, guest = None)
        default, parametrized, and copy constructor.\n 
        takes in nothing for default constructor.\n 
        takes in room, balance, and hotelInfo for a parametrized constructor.\n
        takes in a Guest class to make a copy of itself.

    def checkIn(self)
        check guest into a hotel room

    def checkOut(self)
        check guest out of a hotel room

    def setRoom(self, room)
        sets the guest to have a certain room

    def getRoom(self)
        gets the room the guest is staying in

    def getBalance(self)
        gets the current balance charged to the Guest's account

    def getHotelInfo(self)
        gets the hotel's current information

    def addCharges(self, payment)
        adds to the Guest's balance for a given transaction

    def __repr__(self)
        prints the class in a viewable format
    """
    __name = ''
    __room = None
    __balance = 0
    __hotelInfo = None
    
    def __init__(
        self, name = '', room = None, balance = 0, hotelInfo = [], guest = None):
        """
        default, parametrized, and copy constructor.\n 
        takes in nothing for default constructor.\n 
        takes in room, balance, and hotelInfo for a parametrized constructor.\n
        takes in a Guest class to make a copy of itself.
        
        Parameters
        ----------
        name : str, optional
            Name of the guest
        room : Room, optional
            The room that the guest is staying in
        balance : float, optional
            The balance being charged to the guest's account
        hotelInfo : HotelInfo, optional
            The information containing general hotel information
        guest : Guest, optional
            The guest that you want to copy
        """

        if not isinstance(hotelInfo, list):
            raise TypeError('"hotelInfo" must be of type list')

        if guest != None:
            self.__name = guest.getName()
            self.__room = guest.getRoom()
            self.__balance = guest.getBalance()
            self.__hotelInfo = guest.getHotelInfo()
        else:
            self.__name = name
            self.__room = room
            self.__balance = balance
            self.__hotelInfo = hotelInfo
            
    def checkIn(self, room):
        """
        checks the guest into a hotel room

        Parameters
        ----------
        room : Room
            room which the guest wants to check into
        """         
        if room.getStatus() == 'clean':
            self.__room = room
        else:
            print("room is unavailable")

    def checkOut(self):
        """
        checks the guest out of a hotel room

        """
        room = self.__room
        room.setStatus("dirty")
        self.__room = None

    def setName(self, name):
        """
        changes the name of a guest

        Parameters
        ----------
        name : str, optional
            The name of the guest
        """

        if not isinstance(name, str):
            raise TypeError('"name" must be of type string')
        else:
            self.__name = name
    
    def getName(self):
        """
        returns the name of a guest
        """
        return self.__name
    
    def setRoom(self, room):
        """
        assigns a room for the guest to have

        Parameters
        ----------
        room : Room
            room which the guest is to have
        """
        if not isinstance(room, Room):
            raise TypeError('"room" must be of type Room')
        else:
            self.__room = room

    def getRoom(self):
        """
        gets the room that the guest is staying in
        """
        return self.__room

    def getBalance(self):
        """
        gets the guest's current balance charged to his account
        """
        return self.__balance

    def getHotelInfo(self):
        """
        gets the hotel information the guest can see
        """
        return self.__hotelInfo

    def addCharges(self, payment):
        """
        adds to the guest's balance after buying something

        Parameters
        ----------
        payment : float
            amount being charged to add to guest's balance
        """
        self.__balance += payment

    def __repr__(self):
        """
        returns the class in a printable fashion
        """
        res = {
            'Name': self.getName(),
            'Room': self.__room.__repr__().split('\n'),
            'Balance Charged': self.getBalance(),
            'Hotel Info': self.getHotelInfo()
        }

        res = json.dumps(res, indent=4)

        return res
        
#------------------------------------------------------------------------------
# if __name__ == '__main__':
#     eddie = Guest(name = 'Eddie', hotelInfo=['Pool: 2:00-5:00', "Bar: 7:00-11:00"])
#     rm116 = Room(116, "standard", 2, 'clean')

#     eddie.checkIn(rm116)
#     eddie.addCharges(88.50)

#     print(eddie)
#     print('-------------------')

#     eddie.checkOut()
#     print(eddie)
#------------------------------------------------------------------------------