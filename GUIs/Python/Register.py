from kivy.uix.screenmanager import Screen

from Classes.EasySQL import DB

class RegisterPage(Screen):
    def SignUp(self, usr, pas, fir, las, email):
        try:
            typ = 'Guest'
            DB.insert('Users', [usr, pas, fir, las, email, typ])
            return True
        except:
            print('already exists')
            return False