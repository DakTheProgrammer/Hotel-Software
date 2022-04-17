from kivy.uix.screenmanager import Screen

from Classes.EasySQL import DB

class RegisterPage(Screen):
    """
    The sign up page

    Attributes
    ----------

    Methods
    -------
    SignUp(self, usr, pas, fir, las, email)
        allows user to sign up
    """

    def SignUp(self, usr, pas, fir, las, email):
        """
        allows user to sign up

        Parameters
        ----------
        usr : str
            The username of a user
        pas : str
            The password of a user
        fir : str
            The first name of a user
        las : str
            The last name of a user
        email : str
            The email of a user
        """
        try:
            if usr == '' or pas == '' or fir == '' or las == '' or email == '':
                raise

            typ = 'Guest'
            DB.insert('Users', [usr, pas, fir, las, email, typ])
            return True
        except:
            #returns false if user already exists
            return False

    def on_leave(self):
        self.ids.Fir.text = ''
        self.ids.Las.text = ''
        self.ids.Ema.text = ''
        self.ids.Usr.text = ''
        self.ids.Pword.text = ''
        self.ids.Error.visable = 'False'