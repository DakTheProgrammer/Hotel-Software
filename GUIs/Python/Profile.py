
from kivy.uix.screenmanager import Screen
from GUIs.Python.ImageButton import IButton
from Classes.EasySQL import DB

class ProfilePage(Screen):
    #Need the username of the account in order to get their information
    def getUser(self, username):
        self.user = username
        #gets user information needed to display
        self.Info = DB.run(f"""SELECT First, Last, Email, Type FROM Users
         WHERE Username = '{username}'""")
        #Combine information into one list
        self.Info = list(self.Info[0])

        #User is a Guest
        if(self.Info[3] == "Guest"):
            member = DB.run(f"""SELECT Member FROM Guest WHERE Username = '{username}'""")
            self.Info.append(''.join(list(member[0])))  #yes this looks terrible but it works
             #Set up the interface using the given information
            self.setImage()
        else:
            role = DB.run(f"""SELECT Status FROM Employee WHERE Username = '{username}'""")
            self.Info.append(role[0][0])
            employee = self.Info[3]
            if(employee == 'Attendant'):
                self.ids.Picture.source = 'images/AttProfilePic.png'
            if(self.Info[-1] == 1):
                self.Info[-1] = 'Active'
            else:
                self.Info[-1] = 'Off the Clock'

        self.setName()
        self.setInfo()

    def on_pre_enter(self):
        home = IButton(
                source = 'images/HomeIcon.png', 
                size_hint = (.2,.2), 
                pos_hint  = {"x":0.81, "top":0.6}, 
            )
        home.bind(on_press = self.Home)
        self.add_widget(home)
        self.balance = DB.run(f"""SELECT Balance FROM Guest WHERE Username = '{self.user}'""")
        self.setBalance()


    def setImage(self):
        self.ids.Picture.source = f"images/{self.Info[-1]}Mem.png"

    def setName(self):
        self.ids.Name.text = f"[color=e1c699][b][u]Name:[/u][/b][/color]\n    {self.Info[0]} {self.Info[1]}"
        if(self.Info[3] != 'Guest'):
            self.ids.Name.pos_hint = {'center_x': .5, 'center_y': .8}

    def setInfo(self):
        if(self.Info[3] == 'Guest'):
            self.ids.Info.text =  f"[color=e1c699][b][u]Email:[/u][/b][/color]\n              {self.Info[2]}"+\
                                   f"\n[color=e1c699][b][u]Account:[/u][/b][/color]\n              {self.Info[3]}"+\
                                    f"\n[color=e1c699][b][u]Membership:[/u][/b][/color]\n              {self.Info[-1]} Status"
        else:
            self.ids.Info.text =  f"[color=e1c699][b][u]Email:[/u][/b][/color]\n              {self.Info[2]}"+\
                                   f"\n[color=e1c699][b][u]Assignment:[/u][/b][/color]\n              {self.Info[3]}"+\
                                    f"\n[color=e1c699][b][u]Status:[/u][/b][/color]\n              {self.Info[-1]}"
        

    def setBalance(self):
        if(self.Info[3] == 'Guest'):
            self.ids.Balance.text = "[color=e1c699][b][u]Charges:[/u][/b][/color]   ${:.2f}".format(self.balance[0][0])
        else:
            self.ids.Balance.text = ''

    def Home(self, widget):
        self.parent.current = f'{self.Info[3]}Page'