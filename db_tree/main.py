class Tree:
    def __init__(self, root):
        self.root = root
        self.childs = []

    def addNode(self, node):
        self.childs.append(node)

    def research(self, indices):
        if len(indices) > 0:
            node = self.childs[indices[0] % len(self.childs)]
            print(node.data)

            for index in indices[1:]:
                if node.childs:
                    node = node.childs[index % len(node.childs)]
                    print(node.data)


class Node:
    def __init__(self, data=None):
        self.data = data
        self.childs = []

    def addNode(self, node):
        self.childs.append(node)


root = Tree('abc')
root.addNode(Node('A'))
root.addNode(Node('B'))

root.childs[0].addNode(Node('1'))
root.childs[0].addNode(Node('2'))

root.childs[1].addNode(Node('asd'))
root.childs[1].addNode(Node('asdasd'))

root.childs[0].childs[1].addNode(Node('final'))
root.childs[0].childs[1].addNode(Node('final1'))

root.research([-1, 1, 2, 0 ,3 ,4])
