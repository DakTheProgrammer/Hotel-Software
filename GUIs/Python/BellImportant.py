from kivy.uix.screenmanager import Screen
from kivymd.uix.datatables import MDDataTable
from kivy.uix.image import Image
from kivy.metrics import dp

from Classes.EasySQL import DB

class BellImportantPage(Screen):
    table = None 

    def on_pre_enter(self):
        self.loading = Image(
            source='images/Loading.jpg',
            size_hint=(None, None),
            size=(400, 400),
            pos_hint ={'center_x': 0.5, 'center_y': 0.575},
            )

        self.add_widget(self.loading)

    def on_enter(self):
        #needed for a bug fix with kivy
        if self.table == None:
            query = 'Select * FROM Important'
            info = DB.run(query)

            self.table = MDDataTable(
                pos_hint = {'center_x': 0.5, 'center_y': 0.575},
                size_hint =(0.9, 0.75),
                check = False,
                column_data = [
                    ("First Name", dp(45)),
                    ("Last Name", dp(45)),
                    ('Role', dp(45))
                ],
                row_data = [
                    
                ]
            )

            for items in info:
                self.table.row_data.append(items)

            self.add_widget(self.table)

        self.remove_widget(self.loading)

    def up(self):
        self.parent.current = 'BellhopPage' #this line right here says what is wrong with kivy as a GUI library
        self.parent.current = 'BellImportantPage'

    def on_pre_leave(self):
        self.remove_widget(self.table)
        self.table = None