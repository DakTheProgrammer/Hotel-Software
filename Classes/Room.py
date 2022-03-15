class Room:
    __roomNumber = None
    __roomType = None
    __numOfBeds = None
    __status = None

    def __init__(self, roomNumber, roomType, numOfBeds, status):
        self.__roomNumber = roomNumber
        self.__roomType = roomType.title()
        self.__numOfBeds = numOfBeds

        if status not in ["clean", "dirty", "out of order"]:
            raise ValueError("Invalid status: must be clean, dirty, or out of order")
        self.__status = status

    def setRoomNumber(self, roomNumber):
        self.__roomNumber = roomNumber
    
    def getRoomNumber(self):
        return self.__roomNumber

    def setRoomType(self, roomType):
        self.__roomType = roomType.title()
    
    def getRoomType(self):
        return self.__roomType

    def setNumOfBeds(self, numOfBeds):
        self.__numOfBeds = numOfBeds
    
    def getNumOfBeds(self):
        return self.__numOfBeds

    def setStatus(self, status):
        self.__status = status
    
    def getStatus(self):
        return self.__status

    def __repr__(self):
        return f"""
        Room Number: {self.__roomNumber}
        Room Type: {self.__roomType}
        Number of Beds: {self.__numOfBeds}"""

if __name__ == '__main__':
    room = Room("521", "Regular", "7", "clean")

    print(room)