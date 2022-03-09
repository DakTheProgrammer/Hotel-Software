import sqlite3

class SQL:
    """
    A class used to help with database management

    Methods
    -------
    __init__(self)
        sets the __cursor and __connection 

    run(self, query)
        runs a given query

    printQuery(self, query)
        prints a query result

    insert(self, table, values)
        inserts a row into a table

    getTables(self)
        gets a list of tables

    getColumns(self, table)
        gets columns present in a given table

    getAllFromTable(self, table)
        gets all the entries in a table
    """
    def __init__(self):
        """
        default constructor that sets cursor and connection to DB
        """

        self.__con = sqlite3.connect('SQLite\Databases\Hotel.sqlite')
        self.__cur = self.__con.cursor()

    def run(self, query):
        """
        runs a given query

        Parameters
        ----------
        query : str
            The query you want to run
        """

        try:
            self.__cur.execute(query)
            self.__con.commit()
            return self.__cur.fetchall()
        except:
            print('Bad query')
            raise

    def printQuery(self, query):
        """
        prints the results of a given query

        Parameters
        ----------
        query : str
            The query you want to run
        """

        try:
            for row in self.__cur.execute(query):
                print(row)
        except:
            print('Bad query')
            raise

    def insert(self, table, values):
        """
        inserts values into a table

        Parameters
        ----------
        table : str
            The table you want to insert into
        value : list
            List of things you want to insert in order
        """

        try:
            col = self.getColumns(table)
            query = 'INSERT INTO %s (%s) VALUES(%s)' % (table, ', '.join(col),
             '?,' * (len(values) - 1) + '?')
            self.__cur.execute(query, values)
            self.__con.commit()
        except:
            raise

    def getTables(self):
        """
        returns a list of tables in the database
        """

        try:
            self.__cur.execute(
                "SELECT name FROM sqlite_master WHERE type='table'")
            return self.__cur.fetchall()
        except:
            print('No tables')
            raise

    def getColumns(self, table):
        """
        returns the columns in a table

        Parameters
        ----------
        table : str
            The table you want to see the columns of
        """
        try:
            ret = []
            for col in self.__cur.execute(
                "SELECT * FROM %s" % table).description:
                ret.append(col[0])
            return(ret)
        except:
            print('Invalid table')
            raise

    def getAllFromTable(self, table):
        """
        returns the entire table

        Parameters
        ----------
        table : str
            The table you want to see
        """

        try:
            self.__cur.execute("SELECT * FROM %s" % table)
            return self.__cur.fetchall()
        except:
            print('Invalid table')
            raise

#global variable of the class that deals with the Database
DB = SQL()