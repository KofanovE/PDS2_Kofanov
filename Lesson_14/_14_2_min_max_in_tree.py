"""
Task_2. Додайте до класу Tree  методи пошуку мінімального і максимального значення елементів в бінарному дереві пошуку .
"""


    #
    # def min_nod(self):
    #     if  self.left:
    #         return self.left.min_nod()
    #     else:
    #         return self.id_node
    #
    # def max_nod(self, id_node:Tree_1()):
    #     print(1)
    #     if  id_node.right:
    #         print(2)
    #         return max_nod(id_node)
    #     else:
    #         print(3)
    #         return id_node





class Tree():

    def __init__(self, id_node):
        self.id_node = id_node
        self.left = None
        self.right = None


    def __str__(self):
        return str(self.id_node)

    # Добавлений код.
    #__________________________________________________
    # def min_nod(self, id_nod):
    #     self.start_nod = self.findval(id_nod) #Потрібен саме дочірній атрибут ноду
    #     return self.start_nod
    #


    # Цей метод написаний кров'ю...
    # Функція повертає мінімальне значення з будь-якої гілки дерева
    def min_nod(self, id_node = None):
        if not id_node:
            id_node = self.id_node
        if id_node < self.id_node:
            if self.left is None:
                return None
            elif self.left == id_node:
                if self.left.left:
                    return self.left.left.min_nod()
                return self.left
            return self.left.min_nod(id_node)
        elif id_node > self.id_node:
            if self.right is None:
                return None
            elif self.right == id_node:
                if self.right.left:
                    return self.right.left.min_nod()
                return self.right
            return self.right.min_nod(id_node)
        else:
            if self.left:
                return self.left.min_nod()
            return self.id_node




    # def min_nod(self, id_nod):
    #     self.id_node = id_nod
    #     if id_nod.left:
    #         return min_nod(id_nod.left)
    #     return id_nod

    # def min_nod(self, nod = None):
    #     if nod:
    #
    #     if  self.left:
    #         return self.left.min_nod()
    #     else:
    #         return self.id_node
    #
    # def max_nod(self, id_nod):
    #     self.id_node = id_nod
    #     if self.id_node.right:
    #         return max_node(id_node.right)
    #     return id_node
    #__________________________________________________

    # Method to add list od nodes
    def add_list(self, list_):
        for id_node in list_:
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
            print(str(self.id_node) + ' is found')



    # Print the tree
    def print_tree(self):
        if self.left:
            self.left.print_tree()
        if self.id_node:
            print(self.id_node),
        if self.right:
            self.right.print_tree()



tree = Tree(8)
tree.add_list([3, 1, 6, 10, 14, 13, 7, 4])
print(tree.min_nod(6))

