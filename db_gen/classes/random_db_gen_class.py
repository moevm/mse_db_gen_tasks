from random_number_sequence_generator.random_num_seq_gen import RandomNumberSequenceGenerator
from db_tree.db_tree_class import Tree, Node

faker_config = ['name', 'street_address', 'city', 'state', 'zipcode', 'country', 'company', 'job_title', 'phone', 'ssn',
                'email', 'month', 'year', 'weekday', 'date', 'time', 'latitude', 'longitude', 'license_plate']


class RandomDBGen:
    def __init__(self, sequence: RandomNumberSequenceGenerator, tables_limit=10, columns_limit=5, rows_limit=20):
        self.sequence = sequence
        self.seq_list = []
        self.tables_limit = tables_limit
        self.columns_limit = columns_limit
        self.rows_limit = rows_limit
        self.tree = Tree()

        def flat_map_seq(y): return list(set([abs(self.sequence.next()) % len(faker_config) for i in range(y)]))

        self.seq_list.append(abs(self.sequence.next()) % (self.tables_limit - 1) + 1)
        for x in range(self.seq_list[0]):
            next_num = abs(self.sequence.next()) % self.columns_limit + 1
            table_list = flat_map_seq(next_num)
            self.seq_list.append([table_list, self.sequence.next() % self.rows_limit])

    def return_tree(self):
        for x in range(1, len(self.seq_list)):
            new_node = Node(faker_config[self.seq_list[x][0][0]], self.seq_list[x][1])
            for j in self.seq_list[x][0]:
                new_node.addData(faker_config[j], 'varchar')
            self.tree.addNode(new_node)
        return self.tree
    # load to json