from kivy.uix.screenmanager import Screen
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivy.uix.image import Image

from Classes.EasySQL import DB

class AttendantCheckingPage(Screen):
    table = None
    row_check = []

    def on_pre_enter(self):
        self.loading = Image(
            source = 'images/Loading.jpg',
            size_hint = (None, None),
            size = (400, 400),
            pos_hint = {'center_x': 0.5, 'center_y': 0.575},
            )

        self.add_widget(self.loading)

    def on_enter(self):
        self.row_check = []

        #needed for a bug fix with kivy
        if self.table == None:
            query = 'SELECT x.First, x.Last, y.Room, x.Member FROM Guest AS x JOIN Bags AS y ON (x.username = y.username)'
            info = DB.run(query)

            self.table = MDDataTable(
                pos_hint = {'center_x': 0.5, 'center_y': 0.575},
                size_hint =(0.9, 0.75),
                check = True,
                use_pagination=True,
                rows_num = 7,
                column_data = [
                    ("First Name", dp(30)),
                    ("Last Name", dp(30)),
                    ('Room', dp(30)),
                    ('Type', dp(30)),
                ],
                row_data = [
                    
                ]
            )

            self.table.bind(on_check_press=self.on_check_press)

            for items in info:
                self.table.row_data.append(items)

            self.add_widget(self.table)

        self.remove_widget(self.loading)

    def up(self):
        self.parent.current = 'AttendantPage' #this line right here says what is wrong with kivy as a GUI library
        self.parent.current = 'AttendantCheckingPage'

    def on_check_press(self, instance_table, current_row):
        if current_row in self.row_check:
            self.row_check.remove(current_row)
        else:
            self.row_check.append(current_row)

    def on_pre_leave(self):
        self.remove_widget(self.table)
        self.table = None