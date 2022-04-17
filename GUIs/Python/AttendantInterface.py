from typing import no_type_check
from kivy.uix.screenmanager import Screen
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivy.factory import Factory
from kivy.uix.image import Image
from GUIs.Python.ContactEmployee import ContactEmployee
from Classes.EasySQL import DB

class AttendantInterfacePage(Screen):
    table = None
    ow_check = [] 

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
                self.table.row_data.append(items)

            self.add_widget(self.table)

        self.remove_widget(self.loading)

    def up(self):
        self.parent.current = 'AttendantPage' #this line right here says what is wrong with kivy as a GUI library
        self.parent.current = 'AttendantInterfacePage'

    def on_check_press(self, instance_table, current_row):
        if current_row in self.row_check:
            self.row_check.remove(current_row)
        else:
            self.row_check.append(current_row)

    def on_pre_leave(self):
        self.remove_widget(self.table)
        self.table = None
    
    def contact(self):
        self.messenger = ContactEmployee()
        self.messenger.open()

    
    def sendMessage(self):
        self.message = self.messenger.getMessage()
        if(self.messenger.hasMessage is True):
            for row in self.row_check:
                query = f'Select Message FROM Messages WHERE Username = "{row[0]}"'
                email = DB.run(query)
                email = ''.join(list(email[0])) #Yes this looks stupid but it does what I need it to do
                if(email != 'None'):
                    email = f"{email}, {self.message}"
                else:
                    email = self.message
                query = f'UPDATE Messages SET Message = "{email}" WHERE Username = "{row[0]}"'
                DB.run(query)
        self.parent.current = "AttendantPage"
        Factory.MessageSent().open()