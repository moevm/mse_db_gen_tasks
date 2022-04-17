import json

class Node:
    def __init__(self, name, typename=None, childs=None):
        self.name = name
        self.typename = typename
        self.childs = {}
        self.link = {}

    def addNode(self, node):
        self.childs[node.name] = node

    def setLink(self, link):
        self.link = link

class Tree:
    def __init__(self):
        self.root = Node('root')

    def addNode(self, node):
        self.root.addNode(node)

    def loadJSON(self, path, db_generator=None):
        with open(path) as file:
            f = json.load(file)

        for data in f:
            values_str = ""
            self.root.addNode(Node(data))
            if "fields" in f[data]:
                for field in f[data]["fields"].items():
                    self.root.childs[data].addNode(Node(field[0], field[1]))
                    values_str += field[0] + " " + field[1] + ","

            if "foreign" in f[data]:
                for key, item in f[data]["foreign"].items():
                    self.root.childs[data].childs[key].setLink(item)
                    values_str += f"foreign key ({key}) references {list(item.keys())[0]}({list(item.values())[0]}),"

            if db_generator:
                db_generator.add_table(data, values_str[:-1])


    def export_to_dict(self):
        data = {}
        for table in self.root.childs.values():
            fields = {}
            foreign = {}
            for child in table.childs.values():
                fields[child.name] = child.typename
                if child.link:
                    foreign[child.name] = child.link
            data[table.name] = {"fields": fields, "foreign": foreign}
        return data

    def saveJSON(self, path):
        with open(path, 'w') as outfile:
            json.dump(self.export_to_dict(), outfile)

    def research(self, indices):
        if len(indices) > 0:
            node = self.root.childs[indices[0] % len(self.root.childs)]
            print(node.data)

            for index in indices[1:]:
                if node.childs:
                    node = node.childs[index % len(node.childs)]
                    print(node.data)