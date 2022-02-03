import sqlite3

class SQL:
    def __init__(self):
        self.con = sqlite3.connect('SQLite\Database\Hotel.sqlite')
        self.cur = self.con.cursor()

    def run(self, query):
        try:
            self.cur.execute(query)
            self.con.commit()
            return self.cur.fetchall()
        except:
            return 'Bad query'

    def printQuery(self, query):
        try:
            for row in self.cur.execute(query):
                print(row)
        except:
            print('Bad query')

    def insert(self, table, values):
        ...

    def update(self, table, key, values):
        ...
    
    def delete(self, table, key):
        ...

DB = SQL()