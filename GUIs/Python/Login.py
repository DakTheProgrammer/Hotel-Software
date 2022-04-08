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

            #if a guest go to guest page(pages indexed by numbers)
            if res[5] == 'Guest':
                page = 2
            elif res[5] == 'Manager':
                page = 7
            elif res[5] == 'Attendant':
                page = 3
            elif res[5] == 'Bellhop':
                page = 6
            elif res[5] == 'Room Service':
                page = 8
            
            return page
        else:
            return False

    def on_leave(self):
        self.ids.Usr.text = 'Username'
        self.ids.Pword.text = 'Password'
        self.ids.Error.visable = False
        