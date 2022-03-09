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
            #formating response
            res = list(res[0])

            #if a guest go to guest page
            if res[5] == 'Guest':
                res.append(2)
            
            return list(res)
        else:
            #returns false if user not in DB
            return [False]