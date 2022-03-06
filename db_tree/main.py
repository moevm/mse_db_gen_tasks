class Node:
    def __init__(self, weight, data=None):
        self.weight = weight
        self.data = data
        self.childs = []

    def addNode(self, node):
        self.childs.append(node)

class Tree:
    def __init__(self):
        self.root = Node('root')

    def addNode(self, node):
        self.root.addNode(node)

    def research(self, indices):
        if len(indices) > 0:
            node = self.root.childs[indices[0] % len(self.root.childs)]
            print(node.data)

            for index in indices[1:]:
                if node.childs:
                    node = node.childs[index % len(node.childs)]
                    print(node.data)