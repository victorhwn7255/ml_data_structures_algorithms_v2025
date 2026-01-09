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
      
tree_1 = TreeNode(4)
tree_1.left = TreeNode(2)
tree_1.right = TreeNode(7)
tree_1.left.left = TreeNode(1)
tree_1.left.right = TreeNode(3)
tree_1.right.left = TreeNode(6)
tree_1.right.right = TreeNode(9)

tree_1.print_tree()

def invertTree(root: TreeNode):
  if root is None:
    return None
  
  root.left, root.right = root.right, root.left
  
  invertTree(root.left)
  invertTree(root.right)
  
  return root

def invertTree_BFS(root: TreeNode):
  if root is None:
    return None
  
  queue = [root]
  while len(queue) > 0:
    node = queue.pop(0)
    
    node.left, node.right = node.right, node.left
    
    if node.left:
      queue.append(node.left)
    if node.right:
      queue.append(node.right)
      
  return root

print(invertTree_BFS(tree_1))