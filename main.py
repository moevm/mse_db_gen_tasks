import sqlite3
from random_number_sequence_generator.random_num_seq_gen import RandomNumberSequenceGenerator
from db_gen.classes.db_gen_class import DbGen
from db_gen.classes.random_db_gen_class import RandomDBGen
from select_request_generator.select_request_gen import SelectRequestGenerator


class MainGenerator:
    def __init__(self):
        self.rand_gen = RandomNumberSequenceGenerator()
        self.db_gen = DbGen('results/db_f.db')
        self.select_request_gen = SelectRequestGenerator()

    def generate_tree_with_random_seed(self, console):
        self.rand_gen.init_with_random_seed()
        rdb = RandomDBGen(self.rand_gen)
        rdb.return_tree(console)

    def generate_tree(self, seed, console):
        self.rand_gen.init_with_seed(seed)
        rdb = RandomDBGen(self.rand_gen)
        rdb.return_tree(console)

    def generate_tree_with_relations(self, seed):
        self.rand_gen.init_with_seed(seed)
        rdb = RandomDBGen(self.rand_gen)
        rdb.get_common_columns()

    def generate_select_request(self, console):
        table, columns = self.db_gen.get_random_table_with_columns()
        query = self.select_request_gen.generate_request(columns_list=columns, table_name=table)
        if console == 0:
            self.select_request_gen.save_request(query)
        else:
            print(query)
        # print(DbGen.parse_query(query))

    def dump_db(self, path):
        self.db_gen.dump_db(path)
