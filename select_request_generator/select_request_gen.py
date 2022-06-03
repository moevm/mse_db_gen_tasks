import random
import sqlite3
from faker import Faker


class SelectRequestGenerator:
    def __init__(self, db_gen):
        self.db_gen = db_gen
        self.faker = Faker()
        pass

    def get_random_list(self, columns_list):
        random_columns = []
        random_columns_len = random.randrange(1, len(columns_list)+1)

        while len(random_columns) < random_columns_len:
            selection = random.choice(columns_list)
            if selection not in random_columns:
                random_columns.append(selection)
        return random_columns

    def generate_request(self, columns_list, table_name, include_sort=True, include_where=True):

        random_columns = self.get_random_list(columns_list)
        random_columns_without_types = []

        for random_column in random_columns:
            random_columns_without_types.append(random_column[0])
        random_columns_str = ','.join(random_columns_without_types)

        columns_for_count = self.get_random_list(random_columns)
        columns_for_max = self.get_random_list(random_columns)
        columns_for_min = self.get_random_list(random_columns)
        columns_for_avg = self.get_random_list(random_columns)
        columns_for_sum = self.get_random_list(random_columns)

        for column in columns_for_count:
            random_columns_str = random_columns_str + ",COUNT(" + column[0] + ")"
        for column in columns_for_max:
            random_columns_str = random_columns_str + ",MAX(" + column[0] + ")"
        for column in columns_for_min:
            random_columns_str = random_columns_str + ",MIN(" + column[0] + ")"
        for column in columns_for_avg:
            if column[0] == 'year' or column[0] == 'date' or column[0] == 'time':
                random_columns_str = random_columns_str + ",AVG(" + column[0] + ")"
        for column in columns_for_sum:
            if column[0] == 'year' or column[0] == 'date' or column[0] == 'time':
                random_columns_str = random_columns_str + ",SUM(" + column[0] + ")"

        request = 'SELECT ' + random_columns_str + " FROM " + table_name

        if include_where:
            where_column = random.choice(random_columns)
            condition = random.choice(['=', '>', '<'])
            if where_column[0] != 'year' or where_column[0] != 'date' or where_column[0] != 'time':
                condition = '='
            self.conn = sqlite3.connect(self.db_gen.db_file)
            c = self.conn.cursor()
            c.execute('select ' + where_column[0] + ' from ' + table_name)
            data = c.fetchall()
            request = request + " WHERE " + where_column[0] + " " + condition + ' ' + random.choice(data)[0]

        if include_sort:
            column_for_sort = random.choice(random_columns)
            sort_dir = random.choice(['ASC', 'DESC'])
            request = request + " ORDER BY " + column_for_sort[0] + " " + sort_dir

        return request

    def save_request(self, query):
        file = open("./results/query", "w")
        file.write(query)
