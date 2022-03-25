import sqlite3
from random_number_sequence_generator.random_num_seq_gen import RandomNumberSequenceGenerator
from db_gen.classes.db_gen_class import DbGen


class MainGenerator:
    def __init__(self):
        self.rand_gen = RandomNumberSequenceGenerator()
        self.db_gen = DbGen('db_f.db')

    def generate_tree_with_random_seed(self):
        self.rand_gen.init_with_random_seed()
        # tree generator

    def generate_tree(self, seed):
        self.rand_gen.init_with_seed(seed)
        # tree generator

    def dump_db(self):
        self.db_gen.dump_db()
