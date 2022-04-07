from kivy.uix.screenmanager import Screen
from kivy.clock import Clock
from datetime import date, datetime
from kivy.factory import Factory

from Classes.EasySQL import DB

class GuestPage(Screen):

    def on_pre_enter(self):
        self.ids.clock.text = datetime.today().strftime("%I:%M %p")
        self.ids.date.text = date.today().strftime("%a., %b %d %Y")
        Clock.schedule_interval(self.updates, 0.5)

    def updates(self, args):
        self.ids.clock.text = datetime.today().strftime("%I:%M %p")
        self.ids.date.text = date.today().strftime("%a., %b %d %Y")

    def checkType(self):
        
        if(self.ids.room.text == ' Room: Not Checked In'):
            return 'Check In'
        else:
            return 'Check Out'

    def checked(self):
        if(self.ids.Checking.text == 'Check In'):
            #Temporary until able to see which rooms are available
            self.ids.room.text = ' Room: 118'
        else:
            self.ids.room.text = ' Room: Not Checked In'

        self.ids.Checking.text = self.checkType()

    def getRoomService(self):
        if(self.ids.Checking.text == 'Check In'):   #Cannot access room service until checked into a room
            Factory.NoRoomPop().open()
        else:
            self.parent.current = 'GuestRoomServicePage'

