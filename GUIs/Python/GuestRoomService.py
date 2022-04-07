
from kivy.uix.screenmanager import Screen
from kivy.factory import Factory

from Classes.EasySQL import DB

class GuestRoomServicePage(Screen):
    
    def getCart(self):
        if(self.parent.get_screen('CartPage').isTableEmpty() is True):   #Cannot access room service until checked into a room
            Factory.NoItemsPop().open()
        else:
            self.parent.current = 'CartPage'