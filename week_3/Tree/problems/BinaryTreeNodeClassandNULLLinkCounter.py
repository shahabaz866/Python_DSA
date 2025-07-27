class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

def count_null_links(root):
    if root is None:
        return 1  # NULL link
    return count_null_links(root.left) + count_null_links(root.right)

# Example tree with 5 nodes
#        1
#       / \
#      2   3
#     /     \
#    4       5

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.right = Node(5)

print("Number of NULL links:", count_null_links(root)) 