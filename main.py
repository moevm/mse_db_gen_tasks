import sqlite3
from random_number_sequence_generator.random_num_seq_gen import RandomNumberSequenceGenerator


class MainGenerator:
    def __init__(self):
        self.rand_gen = RandomNumberSequenceGenerator()

    def generate_tree_with_random_seed(self):
        self.rand_gen.init_with_random_seed()
        # tree generator

    def generate_tree(self, seed):
        self.rand_gen.init_with_seed(seed)
        # tree generator
