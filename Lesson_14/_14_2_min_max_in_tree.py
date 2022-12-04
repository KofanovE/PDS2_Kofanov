"""
Task_2. Додайте до класу Tree  методи пошуку мінімального і максимального значення елементів в бінарному дереві пошуку .
"""

class Tree():

    def __init__(self, id_node):
        self.id_node = id_node
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.id_node)

    # Добавлений код.
    #__________________________________________________
    # Method finding of min node
    def min_nod(self):
        if self.left:
            return self.left.min_nod()
        return self.id_node

    # Method finding of max node
    def max_nod(self):
        if self.right:
            return self.right.max_nod()
        return self.id_node
    # __________________________________________________


    # Method adding list of nodes
    def add_list(self, list_):
        for id_node in list_:
            if type(id_node) is int and self.findval(id_node)[-9:] == "Not Found":
                self.insert(id_node)


    # Insert method to create nodes
    def insert(self, id_node):
        if self.id_node:
            if id_node < self.id_node:
                if self.left is None:
                    self.left = Tree(id_node)
                else:
                    self.left.insert(id_node)
            elif id_node > self.id_node:
                if self.right is None:
                    self.right = Tree(id_node)
                else:
                    self.right.insert(id_node)
        else:
            self.id_node = id_node


    # findval method to compare the id_node with nodes
    def findval(self, find_val):
        if find_val < self.id_node:
            if self.left is None:
                return str(find_val) + " Not Found"
            return self.left.findval(find_val)
        elif find_val > self.id_node:
            if self.right is None:
                return str(find_val) + " Not Found"
            return self.right.findval(find_val)
        else:
            return str(self.id_node) + ' Is Found'


    # Print the tree
    def print_tree(self):
        if self.left:
            self.left.print_tree()
        if self.id_node:
            print(self.id_node),
        if self.right:
            self.right.print_tree()


tree = Tree(8)
tree.add_list([3, 1, 6, 10, 14, 13, 7, 4, 10, 2, "cat"])
tree.print_tree()
print(f"Мінімальний нод: {tree.min_nod()}")
print(f"Максимальний нод: {tree.max_nod()}")