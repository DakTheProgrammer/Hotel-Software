import imp
from kivy.app import App
from kivy.uix.widget import Widget

from Classes.EasySQL import DB

class LoginWidget(Widget):
    def Check(self):
        return DB.run('SELECT * FROM GUEST')

class LoginApp(App):
    def build(self):
        return LoginWidget()

    