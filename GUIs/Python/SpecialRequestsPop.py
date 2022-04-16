from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen

class SpecialRequests(Popup):
    buying = False
    
    def Continue(self):
        self.buying = True
        self.dismiss()

    def BuyOut(self):
        return self.buying

    def leave(self):
        return self.ids.request.text
