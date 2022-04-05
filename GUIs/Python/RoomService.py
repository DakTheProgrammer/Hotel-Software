from kivy.uix.screenmanager import Screen
from kivy.clock import Clock
from datetime import date, datetime

from Classes.EasySQL import DB

class ServicePage(Screen):
    def on_pre_enter(self):
        self.ids.clock.text = datetime.today().strftime("%I:%M %p")
        self.ids.date.text = date.today().strftime("%a., %b %d %Y")
        Clock.schedule_interval(self.updates, 0.5)

    def updates(self, args):
        self.ids.clock.text = datetime.today().strftime("%I:%M %p")
        self.ids.date.text = date.today().strftime("%a., %b %d %Y")