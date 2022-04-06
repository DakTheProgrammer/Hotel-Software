from kivy.uix.screenmanager import Screen

from Classes.EasySQL import DB

import geocoder

class HotSpotsPage(Screen):

    def getLat(self):
        location = geocoder.ipinfo('me')
        location = location.latlng
        return location[0]

    def getLon(self):
        location = geocoder.ipinfo('me')
        location = location.latlng
        return location[1]
