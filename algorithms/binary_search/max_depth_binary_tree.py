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
      
tree_1 = TreeNode(3)
tree_1.left = TreeNode(9)
tree_1.right = TreeNode(20)
tree_1.right.left = TreeNode(15)
tree_1.right.right = TreeNode(7)

tree_1.print_tree()

def maxDepth_DFS(root: TreeNode):
  if root is None:
    return 0
  
  depth = 1 + max(maxDepth_DFS(root.left), maxDepth_DFS(root.right))
  
  return depth

def maxDepth_BFS(root: TreeNode):
  if root is None:
    return 0
  queue = [root]
  depth = 0
  
  while len(queue) != 0:
    depth += 1
    level_size = len(queue)
    for _ in range(level_size):
      node = queue.pop(0)
      if node.left:
        queue.append(node.left)
      if node.right:
        queue.append(node.right)
  
  return depth
  

print(maxDepth_DFS(tree_1))
print(maxDepth_BFS(tree_1))