
from kivy.uix.screenmanager import Screen

from Classes.EasySQL import DB

class ProfilePage(Screen):

    #Need the username of the user in order to get their information properly
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

    def getName(self):
        return f"Name: {self.Info[0]} {self.Info[1]}"

    def getEmail(self):
        return f"Email: {self.Info[2]}"

    def getType(self):
        return f"Type: {self.Info[3]}"
    
    def getStatus(self):
        if(self.Info[3] == 'Guest'):
            image = f"images/{self.Info[-1]}Mem.png"
            self.setImage(image)
            return f"Membership: {self.Info[-1]} Status"
        else:
            return f"Job: {self.Info[-1]}"

    def setImage(self, img):
        self.image = img

    def getImage(self):
        return self.image