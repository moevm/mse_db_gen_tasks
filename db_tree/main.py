import json
from db_gen.db_gen_class import DbGen

class Node:
    def __init__(self, name, weight=None, data=None, childs=None):
        self.name = name
        self.weight = weight
        self.data = {}
        self.childs = []

    def addNode(self, node):
        self.childs.append(node)

    def addData(self, key, value):
        self.data[key] = value

class Tree:
    def __init__(self):
        self.root = Node('root')

    def addNode(self, node):
        self.root.addNode(node)

    def loadJSON(self, path, db_generator):
        with open(path) as file:
            f = json.load(file)

        for data in f:
            self.root.addNode(Node(data))
            for item in f[data].items():
                self.root.childs[-1].addData(item[0], item[1])

        for child in self.root.childs:
            print(child.name)
            for item in child.data.items():
                print(item[0] + " " + item[1])

        db_generator.create_db_table(self.root.childs[-1].name, len(self.root.childs[-1].data), list(self.root.childs[-1].data.keys()))

    def saveJSON(self, path):
        data = {}
        for table in self.root.childs:
            childs = {}
            for child in table.data.keys():
                childs[child] = table.data[child]
            data[table.name] = childs
        with open(path, 'w') as outfile:
            json.dump(data, outfile)


    def research(self, indices):
        if len(indices) > 0:
            node = self.root.childs[indices[0] % len(self.root.childs)]
            print(node.data)

            for index in indices[1:]:
                if node.childs:
                    node = node.childs[index % len(node.childs)]
                    print(node.data)