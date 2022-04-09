import sqlite3
from random_number_sequence_generator.random_num_seq_gen import RandomNumberSequenceGenerator
from db_gen.classes.db_gen_class import DbGen
from db_gen.classes.random_db_gen_class import RandomDBGen


class MainGenerator:
    def __init__(self):
        self.rand_gen = RandomNumberSequenceGenerator()
        self.db_gen = DbGen('db_f.db')

    def generate_tree_with_random_seed(self):
        self.rand_gen.init_with_random_seed()
        # tree generator

    def generate_tree(self, seed):
        self.rand_gen.init_with_seed(seed)
        rdb = RandomDBGen(self.rand_gen)
        rdb.return_tree()

        self.db_gen.describe_db()

    def dump_db(self, path):
        self.db_gen.dump_db(path)
