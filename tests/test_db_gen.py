import os.path
import random
import sqlite3
import unittest
from sys import argv
from db_gen.classes.db_gen_class import DbGen


class TestDbGen(unittest.TestCase):

    def setUp(self):
        if len(argv) != 1:
            script, seed = argv
            random.seed(seed)
    
        self.gen = DbGen("test_db_file.db")
        self.rows = random.randrange(3, 10, 1)
        self.all_columns = ['name', 'street_address', 'city', 'state', 'zipcode', 'country', 'company', 'job_title',
                            'phone', 'ssn', 'email', 'year', 'weekday', 'date', 'time', 'license_plate']
        self.columns = random.sample(population=self.all_columns, k=random.randrange(2, len(self.all_columns)))
        self.gen.create_db_table('a', self.rows, self.columns)
        self.gen.conn = sqlite3.connect(self.gen.db_file)

    def test_1_create_table(self):
        cur = self.gen.conn.cursor()
        cur.execute("select * from a")
        values = cur.fetchall()
        self.assertTrue(len(values) == self.rows)
        for i in range(0, self.rows):
            with self.subTest(i=i):
                self.assertTrue(len(values[i]) == len(self.columns))

    def test_2_add_row_to(self):
        fake = self.gen.db_gen.gen_dataframe(num=1, fields=self.columns)
        self.gen.add_row_to('a', fake.values[0])
        fake1 = tuple(fake.values[0])
        cur = self.gen.conn.cursor()
        cur.execute("select * from a")
        values = cur.fetchall()[-1]
        self.assertEqual(values, fake1)

    def test_3_save_db_to_file(self):
        self.gen.save_db_to_file()
        self.assertTrue(os.path.isfile(self.gen.db_file))
