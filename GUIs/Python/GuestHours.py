
from kivy.uix.screenmanager import Screen
from GUIs.Python.ImageButton import IButton

from Classes.EasySQL import DB

class GuestHoursPage(Screen):
    def on_pre_enter(self):
        home = IButton(
                source = 'images/HomeIcon.png', 
                size_hint = (.2,.2), 
                pos_hint  = {"x":0.81, "top":0.6}, 
            )
        home.bind(on_press = self.Home)
        self.add_widget(home)

    def Home(self, widget):
        self.parent.current = "GuestPage"
                
            
    