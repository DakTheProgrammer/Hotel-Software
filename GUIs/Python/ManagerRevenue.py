from kivy.uix.screenmanager import Screen
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp

from Classes.EasySQL import DB

class ManagerRevenuePage(Screen):
    table = None 

    def on_pre_enter(self):
        #needed for a bug fix with kivy
        if self.table == None:
            self.table = MDDataTable(
                pos_hint = {'center_x': 0.5, 'center_y': 0.575},
                size_hint =(0.9, 0.75),
                use_pagination=True,
                rows_num = 7,
                column_data = [
                    ("Date", dp(45)),
                    ("Description", dp(45)),
                    ('Value', dp(45))
                ],
                row_data = [
                    ('4/1/2022', 'Room', '+$265')
                ]
            )

            self.add_widget(self.table)
        
