from kivy.uix.screenmanager import Screen
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivy.uix.image import Image
from GUIs.Python.DisplayPop import Display
from Classes.EasySQL import DB

class MailPage(Screen):
    table = None
    row_check = []
    messages = []

     #Need the username of the account in order to get their information
    def getUser(self, username):
        self.user = username

    def getType(self, emp):
        self.employee = emp

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
            query = f'SELECT Message FROM Messages WHERE Username = "{self.user}" AND Message != "None"'
            info = DB.run(query)
            if(len(info) > 0):
                info = info[0]
            else:
                info = []

            self.table = MDDataTable(
                pos_hint = {'center_x': 0.5, 'center_y': 0.575},
                size_hint =(0.9, 0.75),
                check = True,
                use_pagination=True,
                rows_num = 7,
                column_data = [
                    ('From', dp(45)),
                    ("Message", dp(80)),
                ],
                row_data = [
                    
                ]
            )

            self.table.bind(on_check_press=self.on_check_press)
            if(info != []):
                info =  [tuple(x.split('::')) for x in info[0].split(',/:')]                        
                req = []
                for request in info:
                    request = list(request)                    
                    self.messages.append(request)

                for request in info:
                    request = list(request)
                    query = f"SELECT First, Last FROM Employee WHERE Username = '{request[0]}'"
                    name = DB.run(query)
                    name = f'{name[0][0]} {name[-1][-1]}'
                    request[0] = name
                    if(len(request[-1]) > 30):
                        request[-1] = f'{request[-1][:30]} . . . '
                    req.append(tuple(request))

                for item in req:
                    self.table.row_data.append(item)
            self.add_widget(self.table)

        self.remove_widget(self.loading)

    def up(self):
        self.parent.current = f'{self.employee}Page' #this line right here says what is wrong with kivy as a GUI library
        self.parent.current = 'MailPage'

    def complete(self):
        if self.row_check != []:
            keep = []
            for item in self.table.row_data:
                if(list(item) in self.row_check):
                    continue
                keep.append("::".join(item))
            if(keep != []):  
                keep = ',/:'.join(keep)
                query = f'UPDATE Messages SET Message = "{keep}" WHERE Username = "{self.user}"'
                DB.run(query)
            else:
                query = f'UPDATE Messages SET Message = "None" WHERE Username = "{self.user}"'
                DB.run(query)
        self.up()

    def on_check_press(self, instance_table, current_row):
        if current_row in self.row_check:
            self.row_check.remove(current_row)
        else:
            self.row_check.append(current_row)

    def display(self):
        if(self.row_check != []):
            for message in self.messages:
                if(len(self.row_check[-1][-1]) > 30 and self.row_check[-1][-1][:30] in message[-1]):
                    description = message
                else:
                    if(self.row_check[-1][-1] in message[-1]):
                        description = message
                
            info = Display()
            info.show(description[-1])
            info.open()        

    def on_pre_leave(self):
        self.remove_widget(self.table)
        self.table = None

    def home(self):
        self.parent.current = f'{self.employee}Page' 
