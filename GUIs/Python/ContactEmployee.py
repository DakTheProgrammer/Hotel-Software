from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen

class ContactEmployee(Popup):
    hasMessage = False
    
    def getMessage(self):
        return self.ids.Message.text

    def wroteMessage(self):
        self.hasMessage = True
