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

   
def isSymmetric(root: TreeNode):
  queue = [[root.left, root.right]]
  
  while len(queue) > 0:
    a, b = queue.pop(0)
    if a is None and b is None:
      continue
    elif a is None or b is None:
      return False
    else:
      if a.val != b.val:
        return False
    queue.append([a.left, b.right])
    queue.append([a.right, b.left])
    
  return True

def isSymmetric_DFS(root: TreeNode):
  def dfs(a, b):
    if a is None and b is None:
      return True
    elif a is None or b is None:
      return False
    else:
      if a.val != b.val:
        return False
    return dfs(a.left, b.right) and dfs(a.right, b.left)
  
  return dfs(root.left, root.right)


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)

print(isSymmetric_DFS(root))