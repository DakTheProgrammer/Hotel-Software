from kivy.uix.screenmanager import Screen
from kivy.clock import Clock
from datetime import date, datetime
from kivy.factory import Factory

from Classes.EasySQL import DB

class GuestPage(Screen):

    def on_pre_enter(self):
        self.ids.clock.text = f'[b]{datetime.today().strftime("%I:%M %p")}[/b]'
        self.ids.date.text = f'[b]{date.today().strftime("%a., %b %d %Y")}[/b]'
        Clock.schedule_interval(self.updates, 0.5)

    def updates(self, args):
        self.ids.clock.text = f'[b]{datetime.today().strftime("%I:%M %p")}[/b]'
        self.ids.date.text = f'[b]{date.today().strftime("%a., %b %d %Y")}[/b]'

    def checkType(self):
        
        if(self.ids.room.text == ' [b]Room:[/b] [font=Consolai]Not Checked In[/font]'):
            return 'images/CheckInB2.png'

        else:
            return 'images/CheckOutB2.png'

    def checked(self):
        if(self.ids.Checking.background_normal == 'images/CheckInB2.png'):
            #Temporary until able to see which rooms are available
            self.ids.room.text = ' Room: 118'
        else:
            self.ids.room.text = ' [b]Room:[/b] [font=Consolai]Not Checked In[/font]'

        self.ids.Checking.background_normal = self.checkType()

    def getRoomService(self):
        if(self.ids.Checking.text == 'Check In'):   #Cannot access room service until checked into a room
            Factory.NoRoomPop().open()
        else:
            self.parent.current = 'GuestRoomServicePage'

