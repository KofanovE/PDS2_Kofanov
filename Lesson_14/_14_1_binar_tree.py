"""
Task_1. Додайте до классу Tree метод, який реалізує додавання до бінарного дерева пошуку нових елементів зі списку.
Метод має містити функціонал, який перевіряє дані із списку на відповідність до правил формування бінарного дерева пошуку.
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
    # Method adding list nodes to tree
    def add_list(self, list_):
        for id_node in list_:
            if type(id_node) is int and self.findval(id_node)[-9:] == "Not Found": # Перевірка того, що значення в списку нодів, що додаються - int,
                self.insert(id_node)                                               # та даного нода нема в дереві
    #__________________________________________________


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
