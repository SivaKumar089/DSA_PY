# Day 22: Binary Trees (DFS + BFS Traversals)

from collections import deque

# Step 1: Define the Node class
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Step 2: Create a sample binary tree
"""
        1
       / \
      2   3
     / \   \
    4   5   6
"""

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)


# Step 3: DFS Traversals

# Inorder (Left → Root → Right)
def inorder(root):
    if root:
        inorder(root.left)
        print(root.value, end=' ')
        inorder(root.right)


# Preorder (Root → Left → Right)
def preorder(root):
    if root:
        print(root.value, end=' ')
        preorder(root.left)
        preorder(root.right)


# Postorder (Left → Right → Root)
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.value, end=' ')


# Step 4: BFS Traversal (Level Order)
def level_order(root):
    if not root:
        return
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.value, end=' ')
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


# Step 5: Display outputs
print("Inorder Traversal: ", end='')
inorder(root)

print("\nPreorder Traversal: ", end='')
preorder(root)

print("\nPostorder Traversal: ", end='')
postorder(root)

print("\nLevel Order Traversal: ", end='')
level_order(root)
