from _14_1_binar_tree import Tree

# preorder traversal
def pre_oder(node):
    if node:
        print(node.id_node)
        pre_oder(node.left)
        pre_oder(node.right)

# postorder traversal
def post_order(node):
    if node:
        post_order(node.left)
        post_order(node.right)
        print(node.id_node)

# inorder traversal
def in_order(node):
    if node:
        in_order(node.left)
        print(node.id_node)
        in_order(node.right)

tree = Tree(1)
print(tree.print_tree())
print("_____________________")
tree.left = Tree(2)
print(tree.print_tree())
print("_____________________")
tree.left.left = Tree(3)
print(tree.print_tree())
print("_____________________")
tree.left.right = Tree(4)
print(tree.print_tree())
print("_____________________")
tree.right = Tree(5)
print(tree.print_tree())
print("_____________________")
tree.insert(7)
print(tree.print_tree())
print("_____________________")
tree.insert(12)
print(tree.print_tree())
print("_____________________")
tree.insert(8)
print(tree.print_tree())
print("_____________________")
tree.insert(22)
print(tree.print_tree())
print("_____________________")
tree.insert(14)


print("_____________________")
print(tree.print_tree())