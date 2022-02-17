import sqlite3

class SQL:
    def __init__(self):
        self.con = sqlite3.connect('SQLite\Databases\Hotel.sqlite')
        self.cur = self.con.cursor()

    def run(self, query):
        try:
            self.cur.execute(query)
            self.con.commit()
            return self.cur.fetchall()
        except:
            print('Bad query')
            raise

    def printQuery(self, query):
        try:
            for row in self.cur.execute(query):
                print(row)
        except:
            print('Bad query')
            raise

    def insert(self, table, values):
        try:
            col = self.getColumns(table)
            query = 'INSERT INTO %s (%s) VALUES(%s)' % (table, ', '.join(col), '?,' * (len(values) - 1) + '?')
            self.cur.execute(query, values)
            self.con.commit()
        except:
            raise

    def getTables(self):
        try:
            self.cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
            return self.cur.fetchall()
        except:
            print('No tables')
            raise

    def getColumns(self, table):
        try:
            ret = []
            for col in self.cur.execute("SELECT * FROM %s" % table).description:
                ret.append(col[0])
            return(ret)
        except:
            print('Invalid table')
            raise

    def getAllFromTable(self, table):
        try:
            self.cur.execute("SELECT * FROM %s" % table)
            return self.cur.fetchall()
        except:
            print('Invalid table')
            raise

DB = SQL()