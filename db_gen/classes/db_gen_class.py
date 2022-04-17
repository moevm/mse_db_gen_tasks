from pydbgen import pydbgen
import sqlite3


class DbGen:
    """Class database generator"""

    def __init__(self, db_file_name):
        self.conn = None
        self.db_gen = pydbgen.pydb()
        self.db_file = db_file_name

    def add_column_to(self, table_name, row_name, row_type):
        self.conn = sqlite3.connect(self.db_file)
        cursor = self.conn.cursor()
        cursor.execute(f"ALTER TABLE {table_name} ADD {row_name} {row_type};")
        self.save_db_to_file()

    def add_table(self, table_name, values_data):
        self.conn = sqlite3.connect(self.db_file)
        cursor = self.conn.cursor()
        cursor.execute(f"CREATE TABLE {table_name}({values_data});")
        self.save_db_to_file()

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
        with self.conn:
            self.conn = sqlite3.connect(self.db_file)
            cursor = self.conn.cursor()
            cursor.execute("SELECT name, sql FROM sqlite_master WHERE type='table' ORDER BY name;")
            records = cursor.fetchall()
            table_names = [record[0] for record in records]
            for table_name in table_names:
                cursor.execute(f"PRAGMA table_info({table_name})")
                table_data = cursor.fetchall()
                print("Таблица с названием ", table_name, " содержит в себе ", len(table_data), " столбца:")
                for data in table_data:
                    print(f"\t{data[0] + 1}. Столбец {data[1]} типа {data[2]}")
                cursor.execute(f"SELECT * from {table_name};")
                rows = cursor.fetchall()
                print("Таблица имеет ", len(rows), " записей")
                cursor.execute("PRAGMA foreign_key_list({})".format(self.sql_identifier(table_name)))
                rows = cursor.fetchall()
                for row in rows:
                    print(f"Таблицы {table_name} и {row[2]} связаны по столбцам {row[3]} таблицы {table_name} и {row[4]} таблицы {row[2]}")


    def sql_identifier(self, s):
        return '"' + s.replace('"', '""') + '"'

    def dump_db(self, path='dump_file.txt'):
        self.conn = sqlite3.connect(self.db_file)
        l = ''
        for line in self.conn.iterdump():
            l += line + '\n'
        with open(path, 'w') as dump_file:
            dump_file.write(l)
