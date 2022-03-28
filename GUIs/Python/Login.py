from kivy.uix.screenmanager import Screen

from Classes.EasySQL import DB

class LoginPage(Screen):
    """
    The page that displays the login

    Attributes
    ----------

    Methods
    -------
    Login(self, usr, pas)
        allows user to login
    """
    def Login(self, usr, pas):
        """
        allows user to login

        Parameters
        ----------
        usr : str
            The username of a user
        pas : str
            The password of a user
        """
        
        #gets username and password
        res = DB.run(f"""SELECT * FROM Users
         WHERE Username = '{usr}' AND Password = '{pas}'""")

        if res != []:
            #makes result mutable
            res = list(res[0])

            #if a guest go to guest page
            if res[5] == 'Guest':
                page = 2
            #else if a manager go to manager page
            elif res[5] == 'Manager':
                page = 5
            
            return page