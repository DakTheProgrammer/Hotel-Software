from kivy.uix.screenmanager import Screen
from kivy.clock import Clock
from datetime import date, datetime
from kivy.factory import Factory
from kivy.app import App
from Classes.EasySQL import DB

class GuestPage(Screen):
    username = ''

    def getUsername(self, username):
        #Need what user logged into the system to find out their room number
        #Get what room number has been assigned to the guest's account
        query = f"""SELECT Room FROM Bags WHERE Username = '{username}'"""
        self.room = DB.run(query)[0][0]
        #Get whether the guest has checked in already or not
        query2 = f"""SELECT Checked FROM Room WHERE Room = '{self.room}'"""
        self.check = DB.run(query2)[0][0]
        

    def on_pre_enter(self):
        self.ids.clock.text = f'[b]{datetime.today().strftime("%I:%M %p")}[/b]'
        self.ids.date.text = f'[b]{date.today().strftime("%a., %b %d %Y")}[/b]'
        Clock.schedule_interval(self.updates, 0.5)

        if (self.check == 0):
            self.ids.room.text = ' [b]Room:[/b] [font=Consolai]Not Checked In[/font]'
        else:
           self.ids.room.text =  f' Room: {self.room}'
        
        self.checkType()

    def updates(self, args):
        self.ids.clock.text = f'[b]{datetime.today().strftime("%I:%M %p")}[/b]'
        self.ids.date.text = f'[b]{date.today().strftime("%a., %b %d %Y")}[/b]'

    def checkType(self):
        if(self.check == 0):
            self.ids.Checking.background_normal = 'images/CheckInB.png'

        else:
            self.ids.Checking.background_normal = 'images/CheckOutB.png'

    def checked(self):
        #Person wants to check in to their hotel room
        if(self.check == 0):
            self.check = 1
            self.ids.room.text = f' Room: {self.room}'
            #Update database to show guest has checked in
            query = f'UPDATE Room SET Checked = 1 WHERE Room = "{self.room}"'
            DB.run(query)

        #Person wants to check out of their hotel room
        else:
            self.check = 0
            self.ids.room.text = ' [b]Room:[/b] [font=Consolai]Not Checked In[/font]'
            query = f'UPDATE Room SET Checked = 0 WHERE Room = "{self.room}"'
            DB.run(query)

        #Make sure Checking Button shows the correct Action to take next (Check In or Check Out)
        self.checkType()

    def getRoomService(self):
        if(self.check == 0):   #Cannot access room service until checked into a room
            Factory.NoRoomPop().open()
        else:
            self.parent.current = 'GuestRoomServicePage'

    def getRoom(self):
        return self.room