"""
Task_3. Розширте функціонал класу Tree, додавши в нього метод видалення елементів в бінарному дереві пошуку.
"""

class Tree():

    def __init__(self, id_node):
        self.id_node = id_node
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.id_node)



    def del_node(self, id_node):

        if id_node < self.id_node:   # Якщо заданий аргумент (стартовий вузол пошуку) менше даного вузла:
            if self.left is None:           # Якщо ліва вітка відсутня  - None
                return None
            elif self.left == id_node:      # Якщо ліва дочка являється вузлом, що видаляється..
                if self.left.right:              # Якщо у вузла, що видаляється є права гілка, то вузол заміщається мінімальним нодом цієї гілки
                    left_, right_ = self.left.left, self.left.right
                    self.left = self.left.right.min_nod(None, kil)
                    self.left.left, self.left.right = left_, right_
                elif self.left.left:
                    self.left = self.left.left
                else:
                    self.left = None
            else:
                return self.left.del_node(id_node)    # Продовження пошуку цільового вузла, для початку пошуку мінімального з гілки.
        elif id_node > self.id_node:   # Якщо заданий аргумент більше даного вузла:
            if self.right is None:
                return None
            elif self.right == id_node:
                if self.right.right:
                    left_, right_ = self.right.left, self.right.right
                    self.right = self.right.right.min_nod(None, kil)
                    self.right.left, self.right.right = left_, right_
            elif self.right.left:
                self.right = self.right.left
            else:
                self.right = None
        else:                        # Якщо заданий аргумент == поточному вузлу:
            if self.right:
                left_, right_ = self.left, self.right
                self.id_node = Tree(int(self.right.min_nod(None, kil)))
                self.left, self.right = left_, right_
            elif self.left:
                left_, right_ = self.left.left, self.right.left
                self.id_node = Tree(int(self.left))
                self.left, self.right = left_, right_
            else:
                tree.id_node = None



    def max_nod(self):
        if self.right:
            return self.right.max_nod()
        return self.id_node


    def min_nod(self, id_node = None, kil = False):
        print(id_node, kil)

        if not id_node:               # Якщо не заданий аргумент - пошук з корня дерева
            id_node = self.id_node

        if id_node < self.id_node:   # Якщо заданий аргумент (стартовий вузол пошуку) менше даного вузла:
            if self.left is None:           # Якщо ліва вітка відсутня  - None
                return None

            elif self.left.id_node == id_node:      # Якщо ліва дочка == заданому вузлу початка пошуку - пошук відбувається з даного вузла
                if self.left.left:                         # якщо є продовження лівої гілки, рекурсивний визов ф-Ї пошуку, відносно лівої дочки
                    return self.left.min_nod(None, kil)
                return self.left                          # Якщо у лівої дочки нема продовження лівої гілки, то мінімальний вузол - ліва дочка даного вузла
            return self.left.min_nod(id_node, kil)    # Продовження пошуку цільового вузла, для початку пошуку мінімального з гілки.

        elif id_node > self.id_node:   # Якщо заданий аргумент більше даного вузла:
            if self.right is None:
                return None

            elif self.right.id_node == id_node:
                if self.right.left:
                    return self.right.min_nod(None, kil)
                return self.right
            return self.right.min_nod(id_node, kil)

        else:                        # Якщо заданий аргумент == поточному вузлу:
            print(self.id_node, self.left, self.right)
            if self.left:
                print(100, kil)
                if self.left.left:
                    print(200)
                    return self.left.min_nod(None, kil)
                if kil:
                    print(300)
                    node = self.left
                    self.left = None
                    print("ok")
                    return node
                return self.left
            else:
                print("Fiasko")
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
            return self.id_node


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
# print(tree.max_nod())
# print(tree.min_nod())
# tree.del_node(10)
tree.print_tree()
