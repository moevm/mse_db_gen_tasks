import json

from db_gen.classes.db_gen_class import DbGen


class Node:
    def __init__(self, name, weight=None, typename=None, childs=None):
        self.name = name
        self.weight = weight
        self.typename = typename
        self.childs = {}
        self.link = {}
        self.data = {}

    def add_node(self, node):
        self.childs[node.name] = node

    def add_data(self, key, value):
        self.data[key] = value

    def set_link(self, link):
        self.link = link


class Tree:
    def __init__(self, seed=None):
        self.root = Node('root')
        self.seed = seed

    def add_node(self, node):
        self.root.add_node(node)

    def load_json(self, path, db_generator: DbGen=None):
        with open(path) as file:
            f = json.load(file)

        for data in f["data"]:
            values_str = ""
            self.root.add_node(Node(data))
            if "fields" in f["data"][data]:
                for field in f["data"][data]["fields"].items():
                    self.root.childs[data].add_node(Node(name=field[0], typename=field[1], weight=f["data"][data]["weight"]))
                    values_str += field[0] + " " + field[1] + ","

            if "foreign" in f["data"][data]:
                for key, item in f["data"][data]["foreign"].items():
                    self.root.childs[data].childs[key].set_link(item)
                    values_str += f"foreign key ({key}) references {list(item.keys())[0]}({list(item.values())[0]}),"

            # print(values_str)
            if db_generator:
                weight = f["data"][data]["weight"]
                list_names = list(f["data"][data]["fields"])
                if f["data"][data]["weight"] != 0:
                    # print(data)
                    db_generator.create_db_table(data, f["data"][data]["weight"], list(f["data"][data]["fields"]))
                else:
                    # print('AAAAAAA' + data)
                    db_generator.add_table(data, values_str[:-1])

    def export_to_dict(self):
        data_base = {}
        for table in self.root.childs.values():
            fields = {}
            foreign = {}
            for child in table.data:
                fields[child] = table.data[child]
                # if table.link:
                #     foreign[child.name] = child.link
            data_base[table.name] = {"fields": fields, "foreign": foreign, "weight": table.weight}
        data = {"data": data_base, "seed": self.seed}
        return data

    def save_json(self, path, console):
        if console == 0:
            with open(path, 'w') as outfile:
                json.dump(self.export_to_dict(), outfile)
        else:
            print(self.export_to_dict())

    def research(self, indices):
        if len(indices) > 0:
            node = self.root.childs[indices[0] % len(self.root.childs)]
            print(node.data)

            for index in indices[1:]:
                if node.childs:
                    node = node.childs[index % len(node.childs)]
                    print(node.data)
