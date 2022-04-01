from kivymd.app import MDApp as App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager


#Have to be here so that Kivy can see all classes
from GUIs.Python.Login import LoginPage
from GUIs.Python.Register import RegisterPage
from GUIs.Python.Guest import GuestPage
from GUIs.Python.Attendant import AttendantPage
from GUIs.Python.Bellhop import BellhopPage
from GUIs.Python.Manager import ManagerPage
from GUIs.Python.RoomService import ServicePage
from GUIs.Python.ManagerInterface import ManagerInterfacePage
from GUIs.Python.ManagerSignUp import ManagerSignUpPage
from GUIs.Python.ManagerRoom import ManagerRoomPage
from GUIs.Python.ManagerRevenue import ManagerRevenuePage

class WindowManager(ScreenManager):
    """
    Manages all pages

    Attributes
    ----------

    Methods
    -------
    
    """
    pass

class RootApp(App):
    """
    the root of the application

    Attributes
    ----------

    Methods
    -------
    build(self)
        builds the app based on the Kivy file
    """
    def build(self):
        self.icon = 'images/icon.png'
        return Builder.load_file('GUIs\Kivy\Root.kv')