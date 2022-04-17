from kivy.uix.screenmanager import Screen
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivy.app import App
from Classes.EasySQL import DB
from kivy.uix.image import Image
import ast
from kivy.factory import Factory
from GUIs.Python.SpecialRequestsPop import SpecialRequests

class CartPage(Screen):
    table = None
    row_check = []
    Pay = 0

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
            self.table = MDDataTable(
                pos_hint = {'center_x': 0.5, 'center_y': 0.575},
                size_hint =(0.9, 0.75),
                check = True,
                use_pagination = True,
                rows_num = 7,
                column_data = [
                    ("Item", dp(55)),
                    ("Price", dp(55)),
                ],
                row_data = [

                ]
            )
            self.table.bind(on_check_press=self.on_check_press)

            user = App.get_running_app().root
            room = user.get_screen("GuestPage").getRoom()
            query = f'SELECT Username FROM Room WHERE Room = "{room}"'
            user = DB.run(query)[0][0]
            query = f'SELECT Cart FROM Guest WHERE Username = "{user}"'
            cart = DB.run(query)[0][0]
            cart = ast.literal_eval(cart)

            if(type(cart[0]) == str):
                cart = [cart]

            total = ['Total', 0]
            for item in cart:
                total[1] += float(item[1].strip('$'))
                self.table.row_data.append(item)

            self.pay = total[1]
            total[1] = '${:.2f}'.format(total[1])
            self.table.row_data.insert(0, total)

            self.add_widget(self.table)

        self.remove_widget(self.loading)

    def isTableEmpty(self):
            user = App.get_running_app().root
            room = user.get_screen("GuestPage").getRoom()
            query = f'SELECT Username FROM Room WHERE Room = "{room}"'
            user = DB.run(query)[0][0]
            query = f'SELECT Cart FROM Guest WHERE Username = "{user}"'
            empty = DB.run(query)[0][0]
            if(empty == "Empty"):
                return True
            else:
                return False

    def updateCart(self, item):
        user = App.get_running_app().root
        room = user.get_screen("GuestPage").getRoom()
        query = f'SELECT Username FROM Room WHERE Room = "{room}"'
        user = DB.run(query)
        query = f'SELECT Cart FROM Guest WHERE Username = "{user[0][0]}"'
        cart = DB.run(query)[0][0]
        if(cart == 'Empty'):
            cart = item
        else:
            cart = f'{cart}, {item}'

        query = f'UPDATE Guest SET Cart = "{cart}" WHERE Username = "{user[0][0]}"'
        DB.run(query)

    def requesting(self):
        self.request = SpecialRequests()
        self.request.open()

    def addRequest(self):
        self.message = ''
        if(self.request.BuyOut() is True):
            self.message = self.request.leave()
        else:
            self.message = "None"
        self.checkout()

    def checkout(self):
        user = App.get_running_app().root
        room = user.get_screen("GuestPage").getRoom()
        query = f'SELECT Username FROM Room WHERE Room = "{room}"'
        user = DB.run(query)
        #Remove An Item From the Inventory
        info = []
        for item in self.table.row_data[1:]:
            query = f'SELECT Amount FROM Menu WHERE Name = "{item[0]}" AND Type != "Internet"'
            amount = DB.run(query)
            if(len(amount) > 0):
                amount = int(amount[0][0]) -1
                query = f'UPDATE Menu SET Amount = "{amount}" WHERE Name = "{item[0]}"'
                DB.run(query)
            info.append(item[0])

        info = ', '.join(info)
        
        query = 'SELECT Number FROM Service'
        orderNum = DB.run(query)
        if(len(orderNum) < 1 or int(orderNum[-1][-1]) > 999):
            orderNum = 1
        else:
            orderNum = int(orderNum[-1][-1]) + 1

        
        query = f'INSERT INTO Service (Number, Username, Room, Type, Info) VALUES{orderNum, user[0][0], room, "Service", ":: ".join([info, self.message])}'
        DB.run(query)
        query = f"UPDATE Guest SET Balance = {self.pay} WHERE Username = '{user[0][0]}'"
        DB.run(query)
       
        self.emptyCart()
        #username, room, type, info

    def removeSelected(self):
        #User wanted to remove everything through check boxes
        if(len(self.row_check) == len(self.table.row_data)):
            self.emptyCart()
        else:
            user = App.get_running_app().root
            room = user.get_screen("GuestPage").getRoom()
            query = f'SELECT Username FROM Room WHERE Room = "{room}"'
            user = DB.run(query)
            keep = [i for i in self.table.row_data[1:] if i not in self.row_check]
            keep = f"{keep}"
            query = f'UPDATE Guest SET Cart = "{keep[1:-1]}" WHERE Username = "{user[0][0]}"'
            DB.run(query)
            self.up(2)

    def emptyCart(self):
        user = App.get_running_app().root
        room = user.get_screen("GuestPage").getRoom()
        query = f'SELECT Username FROM Room WHERE Room = "{room}"'
        user = DB.run(query)
        query = f'UPDATE Guest SET Cart = "Empty" WHERE Username = "{user[0][0]}"'
        DB.run(query)
        self.up(1)

    def on_check_press(self, instance_table, current_row):
        if current_row in self.row_check:
            self.row_check.remove(current_row)
        else:
            self.row_check.append(current_row)

    def up(self, num):
        if(num == 1):
            self.parent.current = 'GuestRoomServicePage' #this line right here says what is wrong with kivy as a GUI library

        elif(num == 2):
            self.parent.current = 'GuestRoomServicePage'
            self.parent.current = 'CartPage'

    def on_pre_leave(self):
        self.remove_widget(self.table)
        self.table = None
