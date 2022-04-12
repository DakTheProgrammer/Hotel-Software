from kivy.uix.screenmanager import Screen
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivy.uix.image import Image

from Classes.EasySQL import DB

class InventoryPage(Screen):
    table = None

    def on_pre_enter(self):
        self.loading = Image(
            source = 'images/Loading.jpg',
            size_hint = (None, None),
            size = (400, 400),
            pos_hint = {'center_x': 0.5, 'center_y': 0.575},
            )

        self.add_widget(self.loading)

    def on_enter(self):
        #needed for a bug fix with kivy
        if self.table == None:
            query = 'SELECT * FROM Inventory'
            info = DB.run(query)

            self.table = MDDataTable(
                pos_hint = {'center_x': 0.5, 'center_y': 0.575},
                size_hint =(0.9, 0.75),
                check = False,
                use_pagination=True,
                rows_num = 7,
                column_data = [
                    ("Item", dp(50)),
                    ("Amount", dp(40)),
                    ('Type', dp(45)),
                ],
                row_data = [

                ]   
            )

            for items in info:
                self.table.row_data.append(items)

            self.add_widget(self.table)

        self.remove_widget(self.loading)

    def up(self):
        self.parent.current = 'ServicePage' #this line right here says what is wrong with kivy as a GUI library
        self.parent.current = 'InventoryPage'

    def on_pre_leave(self):
        self.remove_widget(self.table)
        self.table = None