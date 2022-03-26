import json
import os
import unittest

from db_tree.db_tree_class import Tree


class TestTree(unittest.TestCase):

    def setUp(self):
        self.tree = Tree()
        with open('input_tmp.json', 'w') as file:
            json.dump({"table1": {"name": "varchar(50)", "city": "varchar(50)"},
                       "table2": {"name": "varchar(50)", "city": "varchar(50)"}}, file)

        self.tree.loadJSON('input_tmp.json')
        self.tree.saveJSON('output_tmp.json')

        with open('input_tmp.json') as file:
            self.inputFile = json.load(file)

        with open('output_tmp.json') as file:
            self.outputFile = json.load(file)

    def test_loadJSON(self):
        self.assertTrue(self.inputFile == self.outputFile)

    def test_saveJSON(self):
        self.assertTrue(self.outputFile == self.inputFile)

    def test_addNode(self):
        childs_tmp = ['table3', 'table4', 'table5']
        for child in childs_tmp:
            self.tree.addNode(child)
            self.assertEqual(child, self.tree.root.childs[-1])

    def tearDown(self):
        os.remove('input_tmp.json')
        os.remove('output_tmp.json')


if __name__ == "__main__":
    unittest.main()
