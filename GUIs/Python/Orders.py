from kivy.uix.screenmanager import Screen
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivy.uix.image import Image
from GUIs.Python.DisplayPop import Display
from Classes.EasySQL import DB

class OrdersPage(Screen):
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
            users = DB.run('SELECT Username FROM Service')
            info = []
            for user in users:
                query = f'SELECT First, Last FROM Room WHERE Username = "{user[0]}"'
                info.append(DB.run(query)[0])

            query = 'SELECT Room, Type, Info FROM Service'
            info2 = DB.run(query)

            self.table = MDDataTable(
                pos_hint = {'center_x': 0.5, 'center_y': 0.575},
                size_hint =(0.9, 0.75),
                check = True,
                use_pagination=True,
                rows_num = 7,
                column_data = [
                    ("First", dp(30)),
                    ("Last", dp(25)),
                    ("Room", dp(10)),
                    ('Type', dp(15)),
                    ("Info", dp(55))
                ],
                row_data = [
                    
                ]
            )
            req = []
            for request in info2:
                request = list(request)
                if(len(request[-1]) > 30):
                    request[-1] = f'{request[-1][:30]} . . . '
                req.append(tuple(request))

            self.table.bind(on_check_press=self.on_check_press)
            comb = list(x + y for x, y in zip(info, req))
            for items in comb:
                self.table.row_data.append(items)

            self.add_widget(self.table)

        self.remove_widget(self.loading)

    def up(self):
        self.parent.current = 'RoomServicePage' #this line right here says what is wrong with kivy as a GUI library
        self.parent.current = 'OrdersPage'

    def complete(self):
        if self.row_check != []:
            for row in self.row_check:
                query = f'DELETE FROM Service WHERE Room = {row[2]} AND Type = "{row[3]}" AND Info = "{row[4]}"'
                DB.run(query)
      
        self.up()

    def on_check_press(self, instance_table, current_row):
        if current_row in self.row_check:
            self.row_check.remove(current_row)
        else:
            self.row_check.append(current_row)

    def display(self):
        if(len(self.row_check[-1][-1]) > 30):
            query2 = f"""SELECT Info FROM Service WHERE Info LIKE '{self.row_check[-1][-1][:30]}%'"""
        else:
            query2 = f"""SELECT Info FROM Service WHERE Info = '{self.row_check[-1][-1]}'"""
        
        description = DB.run(query2)
        info = Display()
        info.show(description[0][0])
        info.open()        

    def on_pre_leave(self):
        self.remove_widget(self.table)
        self.table = None