from kivy.uix.screenmanager import Screen
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp

from Classes.EasySQL import DB

class ManagerRoomPage(Screen):
    table = None 

    def on_pre_enter(self):
        #needed for a bug fix with kivy
        if self.table == None:
            self.table = MDDataTable(
                pos_hint = {'center_x': 0.5, 'center_y': 0.575},
                size_hint =(0.9, 0.75),
                column_data = [
                    ("Room", dp(45)),
                    ("Occupancy", dp(45)),
                    ('Status', dp(45))
                ],
                row_data = [
                    ('100', 'YELLOW', 'Occupied')
                ]
            )

            self.add_widget(self.table)
        
