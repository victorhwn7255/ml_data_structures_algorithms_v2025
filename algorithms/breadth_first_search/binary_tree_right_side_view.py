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
      
def rightSideView(root: TreeNode) -> list[int]:
  results = []
  queue = []
  index = 0
  
  queue.append(root)
  while index < len(queue):
    level_size = len(queue) - index
    current_level_vals = []
    
    for _ in range(level_size):
      node:TreeNode = queue[index]
      index += 1
      current_level_vals.append(node.val)
      
      if node.left:
        queue.append(node.left)
      if node.right:
        queue.append(node.right)
        
    results.append(current_level_vals[-1])
  
  return results

tree_1 = TreeNode(1)
tree_1.left = TreeNode(2)
tree_1.right = TreeNode(3)
tree_1.left.right = TreeNode(5)
tree_1.right.right = TreeNode(4)

tree_2 = TreeNode(1)
tree_2.left = TreeNode(2)
tree_2.right = TreeNode(3)
tree_2.left.left = TreeNode(4)
tree_2.left.left.left = TreeNode(5)

tree_1.print_tree()
tree_2.print_tree()

print(rightSideView(tree_1))
print(rightSideView(tree_2))
