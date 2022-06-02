import json
import sqlite3
from random_number_sequence_generator.random_num_seq_gen import RandomNumberSequenceGenerator
from db_gen.classes.db_gen_class import DbGen
from db_gen.classes.random_db_gen_class import RandomDBGen
from select_request_generator.select_request_gen import SelectRequestGenerator
import os


class MainGenerator:
    def __init__(self):
        self.rand_gen = RandomNumberSequenceGenerator()
        if os.path.exists("results/db_f.db"):
            os.remove("results/db_f.db")
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

    def generate_tree_one_to_one(self, seed):
        self.rand_gen.init_with_seed(seed)
        rdb = RandomDBGen(self.rand_gen)
        rdb.get_common_columns()
        table_name = self.db_gen.create_one_to_one()
        j = open('results/db_tree.json', 'r')
        jo = json.load(j)
        j.close()
        jo['data'][table_name + '_related'] = {"id": "integer", "data": "varchar", "f_id": "integer"}
        jo['data'][table_name]['foreign'] = {table_name + '_related': 'one_to_one'}
        j = open('results/db_tree.json', 'w')
        json.dump(jo, j)
        j.close()

    def generate_tree_one_to_many(self, seed):
        self.rand_gen.init_with_seed(seed)
        rdb = RandomDBGen(self.rand_gen)
        rdb.get_common_columns()
        table_name = self.db_gen.create_one_to_many()
        j = open('results/db_tree.json', 'r')
        jo = json.load(j)
        j.close()
        jo['data'][table_name + '_related'] = {"id": "integer", "data": "varchar", "f_id": "integer"}
        jo['data'][table_name]['foreign'] = {table_name + '_related': "one_to_many"}
        j = open('results/db_tree.json', 'w')
        json.dump(jo, j)
        j.close()

    def generate_tree_many_to_many(self, seed):
        self.rand_gen.init_with_seed(seed)
        rdb = RandomDBGen(self.rand_gen)
        rdb.get_common_columns()
        table_names = self.db_gen.create_many_to_many()
        j = open('results/db_tree.json', 'r')
        jo = json.load(j)
        j.close()
        jo['data'][table_names[0][0] + '_' + table_names[1][0] + '_related'] =\
            {"id": "integer", "data": "varchar", "f_id_1": "integer", "f_id_2": "integer"}
        jo['data'][table_names[0][0]]['foreign'] = {table_names[0][0] + '_'
                                                    + table_names[1][0] + '_related': "many_to_many"}
        jo['data'][table_names[1][0]]['foreign'] = {table_names[0][0] + '_'
                                                    + table_names[1][0] + '_related': "many_to_many"}
        j = open('results/db_tree.json', 'w')
        json.dump(jo, j)
        j.close()

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
