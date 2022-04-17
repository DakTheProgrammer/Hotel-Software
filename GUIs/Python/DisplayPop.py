from kivy.uix.popup import Popup

class Display(Popup):

    def show(self, described):
        self.ids.Message.text =  str(described)
