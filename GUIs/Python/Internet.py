from kivy.uix.screenmanager import Screen
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp

from Classes.EasySQL import DB

class InternetPage(Screen):
    table = None 

    def on_pre_enter(self):
        #needed for a bug fix with kivy
        if self.table == None:
            self.table = MDDataTable(
                pos_hint = {'center_x': 0.5, 'center_y': 0.575},
                size_hint =(0.9, 0.75),
                check = True,
                column_data = [
                    ("Item", dp(45)),
                    ("Price", dp(45)),
                ],
                #Need to make Amount column editable when I get the time
                row_data = [
                    ('Premium Television', '$25'),
                    ('High Speed Internet', '$15')
                ]
            )

            self.add_widget(self.table)