from kivy.uix.screenmanager import Screen
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivy.uix.image import Image
from kivy.factory import Factory
from GUIs.Python.DescriptionPop import Description
from GUIs.Python.SpecialRequestsPop import SpecialRequests

from Classes.EasySQL import DB

class ToiletriesPage(Screen):
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
            query = 'SELECT Name, Price FROM Menu WHERE Type = "Toiletries" AND Amount > 0'
            info = DB.run(query)

            self.table = MDDataTable(
                pos_hint = {'center_x': 0.5, 'center_y': 0.575},
                size_hint =(0.9, 0.75),
                check = True,
                use_pagination=True,
                rows_num = 7,
                column_data = [
                    ("Name", dp(60)),
                    ('Price', dp(55)),
                ],
                row_data = [
                    
                ],
            )

            self.table.bind(on_check_press=self.on_check_press)

            for items in info:
                self.table.row_data.append(items)

            self.add_widget(self.table)

        self.remove_widget(self.loading)

    def showDescription(self):
        query2 = f"""SELECT Description FROM Menu WHERE Name = '{self.row_check[-1][0]}'"""
        description = DB.run(query2)
        print(description)
        Display = Description()
        Display.show(description[0][0])
        Display.open()

    def requesting(self):
        self.request = SpecialRequests()
        self.request.choosePage('Toiletries')
        self.request.open()

    def addCart(self):
        self.message = self.request.leave()
        if(self.request.BuyOut() is True):
            for item in self.row_check:
                item.append(self.message)
                self.parent.get_screen('CartPage').cart.append(item)
            self.up()

    def on_check_press(self, instance_table, current_row):
        if current_row in self.row_check:
            self.row_check.remove(current_row)
        else:
            self.row_check.append(current_row)

    
    def up(self):
        self.parent.current = 'GuestRoomServicePage' #this line right here says what is wrong with kivy as a GUI library
        self.parent.current = 'ToiletriesPage'

    def on_pre_leave(self):
        self.remove_widget(self.table)
        self.table = None
