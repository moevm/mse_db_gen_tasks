from db_gen.interfaces.db_gen_interface import IDbGen
import pydbgen
from pydbgen import pydbgen


class DbGen(IDbGen):
    def __init__(self, db_file_name):
        self.db_gen = pydbgen.pydbgen()
        self.db_file = db_file_name

    def create_db_table(self, table_name, count_of_rows, column_names):
        self.db_gen.gen_table(db_file=self.db_file, table_name=table_name, fields=column_names, num=count_of_rows)

    def add_row_to(self, table_name, values):
        pass

    def save_db_to_file(self):
        pass
