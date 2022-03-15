class Account:
    """
    A class used to represent an Account

    Attributes
    ----------
    uname : str
        A string to represent an account username
    fname : str
        A string to represent the account holder's first name
    lname : str
        A string to represent the account holder's last name
    email : str
        A string to represent the account holder's email
    password : str
        A string to represent the acccount holder's password
    accountType : str
        A string to represent the account type (Guest or Employee)

    Methods
    -------
    def __init__(self, uname, fname, lname, email, password, accountType):
        self.__uname = uname
        self.__fname = fname
        self.__lname = lname
        self.__email = email
        self.__password = password
        self.__accountType = accountType

    def setUname(self, uname):
        self.__uname = uname
    
    def getUname(self):
        return self.__uname

    def setFname(self, fname):
        self.__fname = fname
    
    def getFname(self):
        return self.__fname

    def setLname(self, lname):
        self.__lname = lname
    
    def getLname(self):
        return self.__lname

    def setEmail(self, email):
        self.__email = email
    
    def getEmail(self):
        return self.__email

    def setPassword(self, password):
        self.__password = password
    
    def getPassword(self):
        return self.__password

    def setAccountType(self, accountType):
        self.__accountType = accountType
    
    def getAccountType(self):
        return self.__accountType
    """

    __uname = None
    __fname = None
    __lname = None
    __email = None
    __password = None
    __accountType = None

    def __init__(self, uname, fname, lname, email, password, accountType):
        self.__uname = uname
        self.__fname = fname.title()
        self.__lname = lname.title()
        self.__email = email
        self.__password = password

        if accountType.title() not in ["Employee", "Guest"]:
            raise ValueError("Account must be a guest account or employee account")
        self.__accountType = accountType.title()

    def setUname(self, uname):
        self.__uname = uname
    
    def getUname(self):
        return self.__uname

    def setFname(self, fname):
        self.__fname = fname.title()
    
    def getFname(self):
        return self.__fname

    def setLname(self, lname):
        self.__lname = lname.title()
    
    def getLname(self):
        return self.__lname

    def setEmail(self, email):
        self.__email = email
    
    def getEmail(self):
        return self.__email

    def setPassword(self, password):
        self.__password = password
    
    def getPassword(self):
        return self.__password

    def setAccountType(self, accountType):
        self.__accountType = accountType.title()
    
    def getAccountType(self):
        return self.__accountType

    def __repr__(self):
        return f"""
        Name: {self.__fname} {self.__lname}
        Email: {self.__email}
        Account Type: {self.__accountType}"""


if __name__ == '__main__':
    Bob = Account("boblikesdogs", "Bob", "Mott", "boblikesdogs@gmail.com", "boblikesdogs1", "guest")

    print(Bob)
