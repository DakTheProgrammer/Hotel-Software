import sqlite3

from kivy.app import App
from kivy.uix.widget import Widget

class LoginWidget(Widget):
    def Check(self):
        con = sqlite3.connect('SQLite\Database\Hotel.sqlite')
        cur = con.cursor()
        cur.execute('SELECT * FROM GUEST')
        con.commit()

        return(cur.fetchall()[0][0])

class LoginApp(App):
    def build(self):
        return LoginWidget()

    