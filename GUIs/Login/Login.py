from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

from Classes.EasySQL import DB

class LoginPage(Screen):
    def Login(self):
        return DB.run('SELECT * FROM Users')

class RegisterPage(Screen):
    def SignUp(self, usr, pas, fir, las, email):
        try:
            typ = 'Guest'
            DB.insert('Users', [usr, pas, fir, las, email, typ])
            return True
        except:
            print('already exists')
            return False

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file('GUIs\Login\Login.kv')

class LoginApp(App):
    def build(self):
        return kv