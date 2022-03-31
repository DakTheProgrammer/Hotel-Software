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
                pos_hint = {'center_x': 0.5, 'center_y': 0.5},
                size_hint =(0.9, 0.6),
                check = True,
                column_data = [
                    ("First Name", dp(30)),
                    ("Last Name", dp(30))
                ],
                row_data = [
                    ('Dakota', 'Wilson'),
                    ('John', 'Doe')
                ]
            )

            self.add_widget(self.table)
        