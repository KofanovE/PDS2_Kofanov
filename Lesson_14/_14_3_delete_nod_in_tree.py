"""
Task_3. Розширте функціонал класу Tree, додавши в нього метод видалення елементів в бінарному дереві пошуку.
"""

from Trees import Tree

class Tree_3(Tree):

    def find_to_del(self, find_val):
        # Ф-я пошуку перероблена для возврату батьківського ноду, відносно видаляємого
        # та флага, з якої він гілки
        if find_val < self.id_node:
            if self.left is None:
                return None
            elif self.left == find_val:
                return self.id_node, False
            else:
                return self.left.findval(find_val)
        elif find_val > self.id_node:
            if self.right is None:
                return None
            elif self.right == find_val:
                return self.id_node, True
            else:
                return self.right.findval(find_val)

    def min_nod(self):
        if  self.left:
            return self.left.min_nod()
        else:
            return self.id_node

    def delete_nod(self, id_nod:Tree, flag):

        father_nod, right_flag = find_to_del(id_nod), flag
        if father_nod:  # нод має цільовий дочірній нод для видалення

            if right_flag:
                delete_nod = father_nod.right
            else:
                delete_nod = father_nod.left

            if delete_nod.right: # Якщо у видаляємого нода є зростаюча по значенням гілка
                change_nod = min_nod(delete_nod.right.right) # Пошук мінімального в цій гілці
            elif delete_nod.left:
                change_nod = delete_nod.left  # Підставлення верхнього дочірнього нода з цієї гілки
            else:
                change_nod = None                        # Видалення ноду без підставки

            delete_nod = change_nod



