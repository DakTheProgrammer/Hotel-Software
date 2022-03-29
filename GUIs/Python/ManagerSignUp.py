from kivy.uix.screenmanager import Screen
from Classes.EasySQL import DB

class ManagerSignUpPage(Screen):
    def Submit(self, fir, las, ema, usr, pas, job):
        if job == 'Job':
            return False
        
        try:
            DB.insert('Users', [usr, pas, fir, las, ema, job])
            return True
        except:
            #returns false if user already exists
            return False

    def on_leave(self):
        self.ids.Fir.text = 'First'
        self.ids.Las.text = 'Last'
        self.ids.Ema.text = 'Email'
        self.ids.Usr.text = 'Username'
        self.ids.Pword.text = 'Password'
        self.ids.spin.text = 'Job'