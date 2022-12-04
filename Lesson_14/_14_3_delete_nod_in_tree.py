"""
Task_3. Розширте функціонал класу Tree, додавши в нього метод видалення елементів в бінарному дереві пошуку.
"""

# Клас бінарного дерева розбитий на два класа: Node і, безпосередньо Tree
class Node:
    def __init__(self, id_node):
        self.id_node = id_node
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    # Добавлений код.
    #__________________________________________________

    # Модернізована ф-я пошуку нода у дереві, що повертає результат пошуку, даний нод і батьківській нод, відносно даного
    def __find(self, node, parent, value):
        if value == node.id_node:
            return node, parent, True
        if value < node.id_node:
            if node.left:
                return self.__find(node.left, node, value)
        if value > node.id_node:
            if node.right:
                return self.__find(node.right, node, value)
        return node, parent, False

    # Ф-я видалення вузла, що не має дочірніх вузлів
    def __del_leaf(self, s, p):
        if p.left == s:
            p.left = None
        elif p.right == s:
            p.right = None

    # Ф-я видалення вузла, що має лише один дочірній вузол
    def __del_one_child(self, s, p):
        if p.left == s:
            if s.left is None:
                p.left = s.right
            elif s.right is None:
                p.left = s.left
        elif p.right == s:
            if s.left is None:
                p.right = s.right
            elif s.right is None:
                p.right = s.left

    # Модернізована ф-я пошуку мінімального  значення, що також повертає батьківський нод
    def __find_min(self, node, parent):
        if node.left:
            return self.__find_min(node.left, node)
        return node, parent

    # Ф-я видалення даного ноду із дерева
    def del_node(self, key):
        s, p, fl_find = self.__find(self.root, None, key)  # Пошук наявності видаляємого ноду
        if not fl_find:           # Якщо не знайдено - вихід із ф-ї
            return None

        if s.left is None and s.right is None:  # Видалення ноду без дочірніх вузлів
            self.__del_leaf(s, p)

        elif s.left is None or s.right is None: # Видалення ноду з єдиною дочкою
            self.__del_one_child(s, p)

        else:                                   # Видалення ноду з 2 дочками
            sr, pr = self.__find_min(s.right, s)   # Пошук мінімального ноду і його батьківського
            s.id_node = sr.id_node                 # Видаляємому ноду присваюється значення мінімального ноду з правої гілки
            self.__del_one_child(sr, pr)           # Видаляється мінімальний нод ф-єю видалення ноду з можливою єдиною дочкою, адже ліва гілка у мінімального виключається

    # __________________________________________________



    # Method finding of min node
    def min_nod(self, node = None):
        if not node:
            node = self.root
        if node.left:
            return self.min_nod(node.left)
        return node.id_node


    # Method finding of max node
    def max_nod(self, node = None):
        if not node:
            node = self.root
        if node.right:
            return self.max_nod(node.right)
        return node.id_node


    # Method adding list of nodes
    def add_list(self, list_):
        for id_node in list_:
            if type(id_node) is int:
                t.insert(Node(id_node))


    # Insert method to create nodes
    def insert(self, obj):
        if self.root is None:
            self.root = obj
            return obj
        s, p, fl_find  = self.__find(self.root, None, obj.id_node)
        if not fl_find and s:
            if obj.id_node < s.id_node:
                s.left = obj
            else:
                s.right = obj
        return obj


    # findval method to compare the id_node with nodes
    def findval(self, find_val):
        node = self.root
        if node == None:
            return str(find_val) + " Not Found"
        if find_val < node.id_node:
            if node.left is None:
                return str(find_val) + " Not Found"
            return self.findval(node.left)
        elif find_val > node.id_node:
            if node.right is None:
                return str(find_val) + " Not Found"
            return self.findval(node.right)
        else:
            return str(node.id_node) + " Is Found"


    # Print the tree
    def print_tree(self, node = None):
        if node is None:
            node = self.root
            if node is None:
                return None
        if node.left:
            self.print_tree(node.left)
        if node.id_node:
            print(node.id_node)
        if node.right:
            self.print_tree(node.right)


v = [10, 5, 7, 16, 13, 2, 20, "cat", 20]
t = Tree()
t.add_list(v)

t.del_node(10)
t.print_tree()
print(f"min: {t.min_nod()}")
print(f"max: {t.max_nod()}")
t.insert(Node(25))
t.print_tree()
print(f"max: {t.max_nod()}")
