from kivy.uix.screenmanager import Screen
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp

from Classes.EasySQL import DB

class ManagerInterfacePage(Screen):
    table = None 

    def on_pre_enter(self):
        #needed for a bug fix with kivy
        if self.table == None:
            self.table = MDDataTable(
                pos_hint = {'center_x': 0.5, 'center_y': 0.575},
                size_hint =(0.9, 0.75),
                check = True,
                column_data = [
                    ("First Name", dp(40)),
                    ("Last Name", dp(30)),
                    ('Role', dp(20)),
                    ('Status', dp(15)),
                    ('Clock In/Out', dp(30))
                ],
                row_data = [
                    ('Dakota', 'Wilson', 'Manager', 'On', '8am')
                ]
            )

            self.add_widget(self.table)
        