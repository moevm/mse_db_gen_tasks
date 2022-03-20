import json


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

    def loadJSON(self, path):
        with open(path) as file:
            f = json.load(file)

        for data in f:
            self.root.addNode(Node(data))
            self.loadJSONImpl(self.root.childs[-1], f[data])

    def loadJSONImpl(self, node, file):
        for item in file.items():
            if type(item[1]) is not dict:
                node.addData(item[0], item[1])
            else:
                node.addNode(Node(item[0]))
                _node = node.childs[-1]
                self.loadJSONImpl(_node, item[1])

    def research(self, indices):
        if len(indices) > 0:
            node = self.root.childs[indices[0] % len(self.root.childs)]
            print(node.data)

            for index in indices[1:]:
                if node.childs:
                    node = node.childs[index % len(node.childs)]
                    print(node.data)
