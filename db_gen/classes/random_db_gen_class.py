import json

from random_number_sequence_generator.random_num_seq_gen import RandomNumberSequenceGenerator
from db_tree.db_tree_class import Tree, Node
from db_gen.classes.db_gen_class import DbGen

faker_config = ['name', 'street_address', 'city', 'state', 'zipcode', 'country', 'company', 'job_title',
                # 'phone',
                'ssn',
                'email',
                # 'month',
                'year', 'weekday', 'date', 'time',
                # 'latitude',UNIQUE
                # 'longitude',
                'license_plate']


class RandomDBGen:
    def __init__(self, sequence: RandomNumberSequenceGenerator, tables_limit=10, columns_limit=10, rows_limit=20):
        self.sequence = sequence
        self.seq_list = []
        self.tables_limit = tables_limit
        self.columns_limit = columns_limit
        self.rows_limit = rows_limit
        self.tree = Tree(sequence.seed)

        def flat_map_seq(y): return list(set([abs(self.sequence.next()) % len(faker_config) for i in range(y)]))

        self.seq_list.append(abs(self.sequence.next()) % (self.tables_limit - 1) + 1)
        for x in range(self.seq_list[0]):
            next_num = abs(self.sequence.next()) % self.columns_limit + 1
            table_list = flat_map_seq(next_num + 1)
            self.seq_list.append([table_list, self.sequence.next() % self.rows_limit])

    def return_tree(self):
        table_names = {}
        for x in range(1, len(self.seq_list)):
            if faker_config[self.seq_list[x][0][0]] not in table_names:
                table_names[faker_config[self.seq_list[x][0][0]]] = 0
            else:
                table_names[faker_config[self.seq_list[x][0][0]]] += 1
            table_name = faker_config[
                self.seq_list[x][0][0]] if table_names[faker_config[self.seq_list[x][0][0]]] == 0 else (
                faker_config[self.seq_list[x][0][0]] + '_' + str(table_names[faker_config[self.seq_list[x][0][0]]]))

            new_node = Node(name=faker_config[
                self.seq_list[x][0][0]] if table_names[faker_config[self.seq_list[x][0][0]]] == 0 else (
                faker_config[self.seq_list[x][0][0]] + '_' + str(table_names[faker_config[self.seq_list[x][0][0]]])),
                            weight=self.seq_list[x][1])
            for j in self.seq_list[x][0]:
                if faker_config[j] in ['year', 'time', 'date']:
                    new_node.add_data(faker_config[j], 'int')
                else:
                    new_node.add_data(faker_config[j], 'varchar')
            self.tree.add_node(new_node)
        self.tree.save_json('results/db_tree.json')
        self.tree.load_json('results/db_tree.json', DbGen('results/db_f.db', self.sequence.seed))

    def get_common_columns(self):
        self.return_tree()
        with open('results/db_tree.json') as json_file:
            data: dict = json.load(json_file)
            sets = dict()
            for i in data["data"].items():
                local_set = set(i[1]["fields"].keys())
                sets[i[0]] = local_set
            key_list = sorted(sets.keys())
            res_dict = dict()
            for i, v in enumerate(key_list):
                if i != len(key_list) - 1:
                    local_intersections = list(sets[key_list[i]].intersection(sets[key_list[i + 1]]))
                    for x in local_intersections:
                        if x not in res_dict:
                            res_dict[x] = [key_list[i], key_list[i + 1]]
                        else:
                            key_list[i] not in res_dict[x] and res_dict[x].append(key_list[i])
                            res_dict[x].append(key_list[i + 1])
