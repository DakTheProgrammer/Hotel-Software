
from kivy.uix.screenmanager import Screen
from GUIs.Python.ImageButton import IButton
from Classes.EasySQL import DB

class ProfilePage(Screen):
    #Need the username of the account in order to get their information
    def getUser(self, username):
        #gets user information needed to display
        self.Info = DB.run(f"""SELECT First, Last, Email, Type FROM Users
         WHERE Username = '{username}'""")
        #Combine information into one list
        self.Info = list(self.Info[0])

        #User is a Guest
        if(self.Info[3] == "Guest"):
            member = DB.run(f"""SELECT Member FROM Guest WHERE Username = '{username}'""")
            self.Info.append(''.join(list(member[0])))  #yes this looks terrible but it works
        else:
            role = DB.run(f"""SELECT Role FROM Employee WHERE Username = '{username}'""")
            self.Info.append(''.join(list(role[0])))

        #Set up the interface using the given information
        self.setImage()
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
        
    def Home(self, widget):
        self.parent.current = "GuestPage"

    def setImage(self):
        self.ids.Picture.source = f"images/{self.Info[-1]}Mem.png"

    def setName(self):
        self.ids.Name.text = f"[color=e1c699][b][u]Name:[/u][/b][/color]\n    {self.Info[0]} {self.Info[1]}"

    def setInfo(self):
        if(self.Info[3] == 'Guest'):
            self.ids.Info.text =  f"[color=e1c699][b][u]Email:[/u][/b][/color]\n              {self.Info[2]}"+\
                                   f"\n[color=e1c699][b][u]Account:[/u][/b][/color]\n              {self.Info[3]}"+\
                                    f"\n[color=e1c699][b][u]Membership:[/u][/b][/color]\n              {self.Info[-1]} Status"
