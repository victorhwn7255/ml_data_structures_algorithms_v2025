import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from utils.tree_utils import print_tree

class TreeNode:
   def __init__(self, val=0, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right
   
   def __str__(self):
      return f"TreeNode({self.val})"
   
   def print_tree(self):
      print_tree(self)
      
def leafSimilar(root1: TreeNode, root2: TreeNode):
  leaf_nodes_1 = []
  leaf_nodes_2 = []
  
  def traverse_to_leaf(root: TreeNode, leaf_list: list):
    if root is None:
      return
    if root.left is None and root.right is None:
      leaf_list.append(root.val)
      return
    traverse_to_leaf(root.left, leaf_list)
    traverse_to_leaf(root.right, leaf_list)
    
  traverse_to_leaf(root1, leaf_nodes_1)
  traverse_to_leaf(root2, leaf_nodes_2)
  
  return leaf_nodes_1 == leaf_nodes_2

tree_1 = TreeNode(3)
tree_1.left = TreeNode(5)
tree_1.right = TreeNode(1)
tree_1.left.left = TreeNode(6)
tree_1.left.right = TreeNode(2)
tree_1.right.left = TreeNode(9)
tree_1.right.right = TreeNode(8)
tree_1.left.right.left = TreeNode(7)
tree_1.left.right.right = TreeNode(4)

tree_2 = TreeNode(3)
tree_2.left = TreeNode(5)
tree_2.right = TreeNode(1)
tree_2.left.left = TreeNode(6)
tree_2.left.right = TreeNode(7)
tree_2.right.left = TreeNode(4)
tree_2.right.right = TreeNode(2)
tree_2.right.right.left = TreeNode(9)
tree_2.right.right.right = TreeNode(8)

print("Tree 1:")
tree_1.print_tree()
print("\nTree 2:")
tree_2.print_tree()

print(leafSimilar(tree_1, tree_2))