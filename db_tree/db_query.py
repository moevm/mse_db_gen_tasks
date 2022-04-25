import sqlite3


class dbQuery:
    def __init__(self, path):
        self.conn = sqlite3.connect(path)
        self.cur = self.conn.cursor()
        self.query = None

    def queryToDB(self, query):
        self.query = query
        self.cur.execute(query)

    def printQuery(self):
        if self.query is not None:
            print(self.cur.fetchall())

    def saveQuery(self, path):
        if self.query is not None:
            saveFile = open(path, "w+")
            saveFile.write(self.query)
            saveFile.close()


# q = dbQuery("D:\\УЧЕБА\\6 семестр\\Разработка ПО\\25.04-1.05\\mse_db_gen_tasks\\db_f.db")
# q.queryToDB("SELECT * FROM street_address;")
# q.printQuery()
# q.saveQuery("D:\\УЧЕБА\\6 семестр\\Разработка ПО\\25.04-1.05\\mse_db_gen_tasks\\query.txt")
