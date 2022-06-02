import uuid

from pydbgen import pydbgen
import sqlite3
import random


class DbGen:
    """Class database generator"""

    def __init__(self, db_file_name, seed=None):
        self.conn = None
        self.db_gen = pydbgen.pydb(seed)
        self.db_file = db_file_name

    def add_column_to(self, table_name, row_name, row_type):
        self.conn = sqlite3.connect(self.db_file)
        cursor = self.conn.cursor()
        cursor.execute(f"ALTER TABLE {table_name} ADD {row_name} {row_type};")
        self.save_db_to_file()

    def add_table(self, table_name, values_data):
        self.conn = sqlite3.connect(self.db_file)
        cursor = self.conn.cursor()
        # print(f"CREATE TABLE {table_name}({values_data});")
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        a = cursor.fetchall()
        cursor.execute(f"CREATE TABLE {table_name}({values_data});")
        self.save_db_to_file()

    def create_db_table(self, table_name, count_of_rows, column_names: list):
        self.db_gen.gen_table(primarykey=column_names[0], db_file=self.db_file, table_name=table_name, fields=column_names, num=count_of_rows)

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

    def get_random_table_with_columns(self):
        self.conn = sqlite3.connect(self.db_file)
        c = self.conn.cursor()
        c.execute("SELECT name, sql FROM sqlite_master WHERE type='table' ORDER BY name;")
        table_names = c.fetchall()
        table = random.choice(table_names)
        data = c.execute("SELECT * FROM " + table[0])
        erase_name = len(table[0])+14
        table_info = table[1][erase_name:-1].split(', ')
        columns = []
        for column in table_info:
            columns.append(column.split(' '))
        return table[0], columns

    def dump_db(self, path='dump_file.txt'):
        self.conn = sqlite3.connect(self.db_file)
        l = ''
        for line in self.conn.iterdump():
            l += line + '\n'
        with open(path, 'w') as dump_file:
            dump_file.write(l)

    @staticmethod
    def parse_query(query: str):
        parsed_query = dict()
        query_words = list(query.split(' '))
        words_count = 0

        def build_string():
            query_string = ''
            query_string += parsed_query['select']
            query_string += ' '.join(parsed_query['asked_columns'])
            query_string += ' ' + parsed_query['table_name']
            query_string += '\n'
            if 'where' in parsed_query:
                query_string += 'по условию '
                query_string += ' '.join(parsed_query['where']) + '\n'
            if 'order_column' in parsed_query:
                query_string += \
                    'в порядке ' + \
                    ('убывания ' if parsed_query['order'] == 'desc' else 'возростания ') + parsed_query['order_column']
            return query_string

        if query_words[0].lower() != 'select':
            return 'Запрос должен содеражть select!'
        else:
            parsed_query[query_words[0].lower()] = 'создать выборку, содержащую '
            words_count += 1
        if query_words[words_count] == '*':
            parsed_query['asked_columns'] = ['все столбцы ']
            words_count += 1
        else:
            column = ''
            columns = []
            while column != 'from':
                column = query_words[words_count].lower()
                if column != 'from':
                    columns.append(column)
                    words_count += 1
            parsed_query['asked_columns'] = columns
        if query_words[words_count].lower() == 'from':
            words_count += 1
            parsed_query['table_name'] = f'из таблицы {query_words[words_count]}'
            words_count += 1

        if words_count == len(query_words):
            return build_string()

        if query_words[words_count].lower() == 'where':
            c_word = ''
            condition = []
            while c_word != 'order':
                if not words_count + 1 > len(query_words) - 1:
                    c_word = query_words[words_count + 1].lower()
                    words_count += 1
                    if c_word != 'order':
                        condition.append(c_word)
                else:
                    break
            parsed_query['where'] = condition
            # words_count += 1

        if words_count == len(query_words) - 1:
            return build_string()

        if query_words[words_count].lower() == 'order':
            words_count += 2
            parsed_query['order_column'] = query_words[words_count].lower()
            words_count += 1
            parsed_query["order"] = query_words[words_count].lower()
        return build_string()

    def create_one_to_one(self):
        with self.conn:
            self.conn = sqlite3.connect(self.db_file)
            # add id column to random existing table
            c = self.conn.cursor()
            c.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;")
            table_names = c.fetchall()
            table_name = random.choice(table_names)[0]
            c.execute(f"alter table {table_name} add column id integer primary key")
            rows_count = c.execute(f"select count(*) from {table_name}").fetchone()[0]
            # create related table
            c.execute(f"create table {table_name}_related (integer id primary key, varchar data, integer f_id, foreign key(f_id) references {table_name}(id))")
            for i in range(rows_count):
                c.execute(f"insert into {table_name}_related values({uuid.uuid4()}, {i})")

    def create_one_to_many(self):
        with self.conn:
            self.conn = sqlite3.connect(self.db_file)
            # add id column to random existing table
            c = self.conn.cursor()
            c.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;")
            table_names = c.fetchall()
            table_name = random.choice(table_names)[0]
            c.execute(f"alter table {table_name} add column id integer primary key")
            rows_count = c.execute(f"select count(*) from {table_name}").fetchone()[0]
            # create related table
            c.execute(
                f"create table {table_name}_related (integer id primary key, varchar data, integer f_id, foreign key(f_id) references {table_name}(id))")
            for i in range(rows_count):
                c.execute(f"insert into {table_name}_related values({uuid.uuid4()}, {random.randint(0, i)})")
