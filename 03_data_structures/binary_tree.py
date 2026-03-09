# =============================================================
# Module 3: Binary Tree Data Structure
# =============================================================
# A Binary Tree is a hierarchical structure where each node
# has at most two children: left and right.
#
# Topics covered:
#   - Binary Tree node and construction
#   - Tree traversals: Inorder, Preorder, Postorder, Level-order
#   - Binary Search Tree (BST) — insert, search, delete
#   - BST properties
#   - Tree height and node count
# =============================================================

from collections import deque

# ---------------------------------------------------------
# Tree Node
# ---------------------------------------------------------
class TreeNode:
    """A single node in a binary tree."""

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return f"TreeNode({self.value})"


# ---------------------------------------------------------
# Binary Tree Traversals
# ---------------------------------------------------------
print("=== Binary Tree Traversals ===")

# Build a sample tree:
#         1
#        / \
#       2   3
#      / \ / \
#     4  5 6  7

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)


def inorder(node):
    """Left → Root → Right (gives sorted order for BST)."""
    if node is None:
        return []
    return inorder(node.left) + [node.value] + inorder(node.right)


def preorder(node):
    """Root → Left → Right (useful for copying/serializing a tree)."""
    if node is None:
        return []
    return [node.value] + preorder(node.left) + preorder(node.right)


def postorder(node):
    """Left → Right → Root (useful for deleting a tree)."""
    if node is None:
        return []
    return postorder(node.left) + postorder(node.right) + [node.value]


def level_order(root):
    """Breadth-First traversal, level by level."""
    if root is None:
        return []
    result, queue = [], deque([root])
    while queue:
        node = queue.popleft()
        result.append(node.value)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result


print(f"Inorder:     {inorder(root)}")
print(f"Preorder:    {preorder(root)}")
print(f"Postorder:   {postorder(root)}")
print(f"Level-order: {level_order(root)}")


def height(node):
    """Return the height of the tree (0 for a single node)."""
    if node is None:
        return -1
    return 1 + max(height(node.left), height(node.right))


def count_nodes(node):
    """Return the total number of nodes."""
    if node is None:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)


print(f"\nHeight:     {height(root)}")
print(f"Node count: {count_nodes(root)}")

# ---------------------------------------------------------
# Binary Search Tree (BST)
# ---------------------------------------------------------
print("\n=== Binary Search Tree (BST) ===")

class BST:
    """
    Binary Search Tree.

    Property: For every node n,
      all values in left subtree  < n.value
      all values in right subtree > n.value
    """

    def __init__(self):
        self.root = None

    # --- Insert ---
    def insert(self, value):
        """Insert a value into the BST."""
        self.root = self._insert(self.root, value)

    def _insert(self, node, value):
        if node is None:
            return TreeNode(value)
        if value < node.value:
            node.left = self._insert(node.left, value)
        elif value > node.value:
            node.right = self._insert(node.right, value)
        # duplicate values are ignored
        return node

    # --- Search ---
    def search(self, value):
        """Return True if value exists in the BST."""
        return self._search(self.root, value)

    def _search(self, node, value):
        if node is None:
            return False
        if value == node.value:
            return True
        if value < node.value:
            return self._search(node.left, value)
        return self._search(node.right, value)

    # --- Delete ---
    def delete(self, value):
        """Remove a value from the BST."""
        self.root = self._delete(self.root, value)

    def _delete(self, node, value):
        if node is None:
            return None
        if value < node.value:
            node.left = self._delete(node.left, value)
        elif value > node.value:
            node.right = self._delete(node.right, value)
        else:
            # Node to delete found
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            # Two children: replace with inorder successor (min of right subtree)
            successor = self._min_node(node.right)
            node.value = successor.value
            node.right = self._delete(node.right, successor.value)
        return node

    def _min_node(self, node):
        """Find the node with the minimum value."""
        while node.left:
            node = node.left
        return node

    # --- Utilities ---
    def inorder(self):
        """Return sorted list of values."""
        return inorder(self.root)

    def height(self):
        return height(self.root)

    def __str__(self):
        return f"BST({self.inorder()})"


bst = BST()
values = [50, 30, 70, 20, 40, 60, 80]
for v in values:
    bst.insert(v)

print(f"BST after inserting {values}:")
print(f"  Inorder (sorted): {bst.inorder()}")
print(f"  Height: {bst.height()}")

print(f"\nSearch 40: {bst.search(40)}")
print(f"Search 99: {bst.search(99)}")

bst.delete(30)
print(f"\nAfter deleting 30: {bst}")

bst.delete(50)
print(f"After deleting root (50): {bst}")

# ---------------------------------------------------------
# Application: Validate a BST
# ---------------------------------------------------------
print("\n=== Application: Validate BST ===")

def is_valid_bst(node, min_val=float('-inf'), max_val=float('inf')):
    """
    Check whether a binary tree is a valid BST.

    Args:
        node: Root of the (sub)tree.
        min_val: Lower bound for current node's value.
        max_val: Upper bound for current node's value.

    Returns:
        bool: True if it is a valid BST.
    """
    if node is None:
        return True
    if not (min_val < node.value < max_val):
        return False
    return (is_valid_bst(node.left, min_val, node.value) and
            is_valid_bst(node.right, node.value, max_val))


print(f"bst.root tree is valid BST: {is_valid_bst(bst.root)}")

# Manually create an invalid BST
bad_root = TreeNode(10)
bad_root.left = TreeNode(5)
bad_root.right = TreeNode(15)
bad_root.right.left = TreeNode(6)   # violates BST: 6 < 10 but is in right subtree
print(f"Manually invalid tree is valid BST: {is_valid_bst(bad_root)}")
