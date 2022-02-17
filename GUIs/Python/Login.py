from kivy.uix.screenmanager import Screen

from Classes.EasySQL import DB

class LoginPage(Screen):
    def Login(self, usr, pas):
        res = DB.run(f"SELECT * FROM Users WHERE Username = '{usr}' AND Password = '{pas}'")

        if res != []:
            res = list(res[0])

            if res[5] == 'Guest':
                res.append(2)
            
            return list(res)
        else:
            return [False]