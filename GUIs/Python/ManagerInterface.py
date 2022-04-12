from kivy.uix.screenmanager import Screen
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivy.uix.image import Image

from Classes.EasySQL import DB

class ManagerInterfacePage(Screen):
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
            query = 'SELECT * FROM Employee'
            info = DB.run(query)

            self.table = MDDataTable(
                pos_hint = {'center_x': 0.5, 'center_y': 0.575},
                size_hint =(0.9, 0.75),
                check = True,
                use_pagination=True,
                rows_num = 7,
                column_data = [
                    ('Username', dp(40)),
                    ("First Name", dp(25)),
                    ("Last Name", dp(25)),
                    ('Role', dp(25)),
                    ('Status', dp(20))
                ],
                row_data = [
                    
                ]
            )

            self.table.bind(on_check_press=self.on_check_press)

            for items in info:
                if items[4] == 1:
                    tup = (items[0], items[1], items[2], items[3], 'Online')
                else:
                    tup = (items[0], items[1], items[2], items[3], 'Offline')

                self.table.row_data.append(tup)

            self.add_widget(self.table)

        self.remove_widget(self.loading)

    def up(self):
        self.parent.current = 'ManagerPage' #this line right here says what is wrong with kivy as a GUI library
        self.parent.current = 'ManagerInterfacePage'

    def remove(self):
        if self.row_check != []:
            
            for row in self.row_check:
                query1 = f'DELETE FROM Employee WHERE Username = "{row[0]}"'
                DB.run(query1)

                query2 = f'DELETE FROM Users WHERE Username = "{row[0]}"'
                DB.run(query2)
      
        self.up()
    
    def on_check_press(self, instance_table, current_row):
        if current_row in self.row_check:
            self.row_check.remove(current_row)
        else:
            self.row_check.append(current_row)

    def on_pre_leave(self):
        self.remove_widget(self.table)
        self.table = None