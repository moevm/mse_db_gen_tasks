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
        val = ''
        j = 0
        for i in values:
            val += "'" + i + "'"
            if j != len(values) - 1:
                val += ', '
            j += 1
        print(val)
        c.execute(f"INSERT INTO {table_name} VALUES ({val})")
        self.conn.commit()
        c.execute(f"select * from {table_name}")
        print(c.fetchall())
        self.save_db_to_file()

    def save_db_to_file(self):
        self.conn.commit()
