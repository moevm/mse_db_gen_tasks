from pydbgen import pydbgen
import sqlite3


class DbGen:
    """Class database generator"""

    def __init__(self, db_file_name):
        self.conn = None
        self.db_gen = pydbgen.pydb()
        self.db_file = db_file_name

    def create_db_table(self, table_name, count_of_rows, column_names):
        self.db_gen.gen_table(db_file=self.db_file, table_name=table_name, fields=column_names, num=count_of_rows)

    def add_row_to(self, table_name, values):
        self.conn = sqlite3.connect(self.db_file)
        c = self.conn.cursor()
        val = "'" + "', '".join(values) + "'"
        c.execute(f"INSERT INTO {table_name} VALUES ({val})")
        self.conn.commit()
        c.execute(f"select * from {table_name}")
        self.save_db_to_file()

    def save_db_to_file(self):
        self.conn.commit()

    def describe_db(self):
        """
        Method for describing database
        """
        with self.conn:
            self.conn = sqlite3.connect(self.db_file)
            c = self.conn.cursor()
            c.execute("SELECT name, sql FROM sqlite_master WHERE type='table' ORDER BY name;")
            meta_data = c.fetchall()
            table_names = [i[0][0] for i in meta_data]
            for j in table_names:
                c.execute(f"PRAGMA table_info({j})")
                data = c.fetchall()
                print(f"Таблица {j} включает в себя следующие столбцы:")
                for d in data:
                    print(f"\t{d[0] + 1}. Столбец {d[1]} типа {d[2]}")

    def dump_db(self):
        self.conn = sqlite3.connect(self.db_file)
        l = ''
        for line in self.conn.iterdump():
            l += line + '\n'
        with open('dump_file.txt', 'w') as dump_file:
            dump_file.write(l)
