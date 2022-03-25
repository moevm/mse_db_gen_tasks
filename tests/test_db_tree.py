import unittest
import json
from db_tree.db_tree_class import Tree


class TestTree(unittest.TestCase):

    def test_loadJSON(self):
        tree = Tree()
        tree.loadJSON('example.json')
        tree.saveJSON('utesttree.json')

        with open('example.json') as file:
            inputFile = json.load(file)

        with open('utesttree.json') as file:
            outputFile = json.load(file)

        self.assertTrue(inputFile == outputFile)

    def test_saveJSON(self):
        tree = Tree()
        tree.loadJSON('example.json')
        tree.saveJSON('utesttree.json')

        with open('example.json') as file:
            inputFile = json.load(file)

        with open('utesttree.json') as file:
            outputFile = json.load(file)

        self.assertTrue(outputFile == inputFile)

    def test_addNode(self):
        tree = Tree()

        childs = ['A', 'B', 'C']
        for child in childs:
            tree.addNode(child)

        self.assertTrue(len(childs) == len(tree.root.childs))
        for i in range(0, len(childs)):
            self.assertTrue(childs[i] == tree.root.childs[i])