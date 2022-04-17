from kivy.uix.screenmanager import Screen
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivy.uix.image import Image
from datetime import datetime

from Classes.EasySQL import DB

class EditServicesPage(Screen):
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
            query = 'SELECT * FROM Inventory'
            info = DB.run(query)
            query = 'SELECT Name, Amount, Type FROM Menu'
            info2 = DB.run(query)

            self.table = MDDataTable(
                pos_hint = {'center_x': 0.5, 'center_y': 0.575},
                size_hint =(0.9, 0.75),
                check = True,
                use_pagination=True,
                rows_num = 7,
                column_data = [
                    ("Item", dp(45)),
                    ("Amount", dp(45)),
                    ('Type', dp(45)),
                ],
                row_data = [
                    
                ]
            )

            self.table.bind(on_check_press=self.on_check_press)

            for items in info:
                self.table.row_data.append(items)
            for items in info2:
                self.table.row_data.append(items)

            self.add_widget(self.table)

        self.remove_widget(self.loading)

    def up(self):
        self.parent.current = 'RoomServicePage' #this line right here says what is wrong with kivy as a GUI library
        self.parent.current = 'EditServicesPage'

    def add(self):
        if self.row_check != []:
            date = datetime.today().strftime('%Y-%m-%d')
            for row in self.row_check:
                query1 = f'UPDATE Inventory SET Amount = (Amount + 1) WHERE Item = "{row[0]}"'
                DB.run(query1)
                query1 = f'UPDATE Menu SET Amount = (Amount + 1) WHERE Name = "{row[0]}"'
                DB.run(query1)

                query2 = f'INSERT INTO Revenue (Date, Description, Value) VALUES (DATE("{date}"), "{row[0]}", -10.99)'
                DB.run(query2)
      
        self.up()

    def remove(self):
        if self.row_check != []:
            for row in self.row_check:
                query = f'UPDATE Inventory SET Amount = (Amount - 1) WHERE Item = "{row[0]}" AND Amount != 0'
                DB.run(query)
                query1 = f'UPDATE Menu SET Amount = (Amount - 1) WHERE Name = "{row[0]}" AND Amount != 0'
                DB.run(query1)
      
        self.up()

    def on_check_press(self, instance_table, current_row):
        if current_row in self.row_check:
            self.row_check.remove(current_row)
        else:
            self.row_check.append(current_row)

    def on_pre_leave(self):
        self.remove_widget(self.table)
        self.table = None