from kivy.config import Config

#prevents user from being able to resize the application must be placed
#above all other kivy imports
Config.set('graphics', 'resizable', False)

from Classes.EasySQL import DB

from kivymd.app import MDApp as App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivy_garden.mapview import MapView

#Have to be here so that Kivy can see all classes
from GUIs.Python.Login import LoginPage
from GUIs.Python.Register import RegisterPage
from GUIs.Python.Guest import GuestPage
from GUIs.Python.Attendant import AttendantPage
from GUIs.Python.AttendantInterface import AttendantInterfacePage
from GUIs.Python.AttendantRoom import AttendantRoomPage
from GUIs.Python.AttChecking import AttendantCheckingPage
from GUIs.Python.Bellhop import BellhopPage
from GUIs.Python.Manager import ManagerPage
from GUIs.Python.RoomService import RoomServicePage
from GUIs.Python.ManagerInterface import ManagerInterfacePage
from GUIs.Python.ManagerSignUp import ManagerSignUpPage
from GUIs.Python.ManagerRoom import ManagerRoomPage
from GUIs.Python.ManagerRevenue import ManagerRevenuePage
from GUIs.Python.EditServices import EditServicesPage
from GUIs.Python.Inventory import InventoryPage
from GUIs.Python.Orders import OrdersPage
from GUIs.Python.BellGuest import BellGuestPage
from GUIs.Python.BellImportant import BellImportantPage
from GUIs.Python.BellLugage import BellLugagePage
from GUIs.Python.GuestHours import GuestHoursPage
from GUIs.Python.HotSpots import HotSpotsPage
from GUIs.Python.GuestRoomService import GuestRoomServicePage
from GUIs.Python.Food import FoodPage
from GUIs.Python.Toiletries import ToiletriesPage
from GUIs.Python.Internet import InternetPage
from GUIs.Python.Cart import CartPage
from GUIs.Python.Profile import ProfilePage
from GUIs.Python.ImageButton import IButton
from GUIs.Python.DescriptionPop import Description
from GUIs.Python.SpecialRequestsPop import SpecialRequests
from GUIs.Python.ContactEmployee import ContactEmployee
from GUIs.Python.DisplayPop import Display
from GUIs.Python.Mail import MailPage



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
    username = None
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
        self.title = 'Hotel Works'
        return Builder.load_file('GUIs\Kivy\Root.kv')

    def on_stop(self):
        query = f'UPDATE Employee SET Status = False WHERE Username = "{self.username}"'
        DB.run(query)