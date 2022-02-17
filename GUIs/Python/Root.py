from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager

#Have to be here so that Kivy can see all classes
from GUIs.Python.Login import LoginPage
from GUIs.Python.Register import RegisterPage
from GUIs.Python.Guest import GuestPage

class WindowManager(ScreenManager):
    pass

class RootApp(App):
    def build(self):
        return Builder.load_file('GUIs\Kivy\Root.kv')