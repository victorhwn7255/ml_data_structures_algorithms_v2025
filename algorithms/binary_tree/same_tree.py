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

tree_1 = TreeNode(1)
tree_1.left = TreeNode(2)
tree_1.right = TreeNode(1)

tree_2 = TreeNode(1)
tree_2.left = TreeNode(1)
tree_2.right = TreeNode(2)

def isSameTree(p: TreeNode, q: TreeNode):
  if p is None and q is None:
    return True
  if p is None or q is None:
    return False
  if p.val != q.val:
    return False
  
  return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

print(isSameTree(tree_1, tree_2))

def isSameTree_BFS(p: TreeNode, q: TreeNode):
  if p is None and q is None:
    return True
  if p is None or q is None:
    return False
  
  queue = [[p, q]]
  
  while len(queue) != 0:
    node1, node2 = queue.pop(0)
    if node1.val != node2.val:
      return False
    
    if node1.left and node2.left:
      queue.append([node1.left, node2.left])
    elif node1.left or node2.left:
      return False
    
    if node1.right and node2.right:
      queue.append([node1.right, node2.right])
    elif node1.right or node2.right:
      return False
      
  return True

print(isSameTree_BFS(tree_1, tree_2))