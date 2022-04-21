from kivy.uix.screenmanager import Screen
from Classes.EasySQL import DB

class ManagerSignUpPage(Screen):
    def Submit(self, fir, las, ema, usr, pas, job):
        if job == 'Job' or usr == '' or pas == '' or fir == '' or las == '' or ema == '':
            return False
        
        try:
            DB.insert('Users', [usr, pas, fir, las, ema, job])
            DB.insert('Employee', [usr, fir, las, job, False])
            return True
        except:
            #returns false if user already exists
            return False

    def on_leave(self):
        self.ids.Fir.text = ''
        self.ids.Las.text = ''
        self.ids.Ema.text = ''
        self.ids.Usr.text = ''
        self.ids.Pword.text = ''
        self.ids.spin.text = 'Job'