from distutils.log import info
from kivy.uix.screenmanager import Screen
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivy.uix.image import Image

from Classes.EasySQL import DB

class BellGuestPage(Screen):
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
        #info = [('Dakota', 'Wilson', '420', 'Gold Member', 'Not Taken'), ('Dakota', 'Wilson', '420', 'Gold Member', 'Not Taken')]
        if self.table == None:
            query = 'SELECT x.First, x.Last, y.Room, x.Member, y.Status FROM Guest AS x JOIN Bags AS y ON (x.username = y.username)'
            info = DB.run(query)

            self.table = MDDataTable(
                pos_hint = {'center_x': 0.5, 'center_y': 0.575},
                size_hint =(0.9, 0.75),
                check = False,
                use_pagination=True,
                rows_num = 7,
                column_data = [
                    ("First Name", dp(30)),
                    ("Last Name", dp(30)),
                    ('Room', dp(20)),
                    ('Type', dp(30)),
                    ('Lugage', dp(25))
                ],
                row_data = [

                ]
            )

            for items in info:
                self.table.row_data.append(items)

            self.add_widget(self.table)

        self.remove_widget(self.loading)