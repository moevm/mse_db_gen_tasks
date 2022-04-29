import sqlite3
from prettytable import PrettyTable


class dbQuery:
    def __init__(self, path):
        self.conn = sqlite3.connect(path)

        self.cur = self.conn.cursor()
        self.tables = []
        self.cur.execute('SELECT name from sqlite_master where type= "table"')
        for table in self.cur:
            self.tables.append(table[0])
        self.query = None

    def queryToDB(self, query):
        # self.cur.execute('SELECT name from sqlite_master where type= "table"')
        #
        # print(self.cur.fetchall())
        self.query = query
        self.cur.execute(query)

    def printQuery(self):
        if self.query is not None:
            columns = self.cur.description
            th = []
            for row in columns:
                th.append(row[0])
            table = PrettyTable(th)
            td = self.cur.fetchall()
            table.add_rows(td)
            print(table)

    def printTables(self):
        for table_name in self.tables:
            query = 'SELECT * FROM ' + table_name
            self.cur.execute(query)
            columns = self.cur.description
            th = []
            for row in columns:
                th.append(row[0])
            table = PrettyTable(th)
            table.title = table_name
            td = self.cur.fetchall()
            table.add_rows(td)
            print(table)

    def printTableNames(self):
        for name in self.tables:
            print(name)

    def saveQuery(self, path):
        if self.query is not None:
            saveFile = open(path, "w+")
            saveFile.write(self.query)
            saveFile.close()


# q = dbQuery("D:\\УЧЕБА\\6 семестр\\Разработка ПО\\25.04-1.05\\mse_db_gen_tasks\\db_f.db")
# q.printTables()
# q.queryToDB('INSERT INTO longitude VALUES ("55,755831°, 37,617673°","2022","12:00PM") ')
# q.printQuery()
# q.printTables()
# q.printTables()
# q.queryToDB("SELECT * FROM street_address;")
# q.printQuery()

# q.saveQuery("D:\\УЧЕБА\\6 семестр\\Разработка ПО\\25.04-1.05\\mse_db_gen_tasks\\query.txt")

