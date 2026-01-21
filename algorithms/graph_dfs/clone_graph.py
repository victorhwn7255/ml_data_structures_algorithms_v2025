class Node:
  def __init__(self, val = 0, neighbors = None):
    self.val = val
    self.neighbors = neighbors if neighbors is not None else []
        
def cloneGraph(node: Node):
  if node is None:
    return None
  
  cloned = {}
  
  def dfs(current: Node):
    if current in cloned:
      return cloned[current]
    copy = Node(current.val)
    cloned[current] = copy
    for neighbor in current.neighbors:
      copy.neighbors.append( dfs(neighbor) )
    
    return copy
  
  return dfs(node)

def cloneGraph_BFS(node: Node):
  if node is None:
    return None
  
  cloned = {}
  queue = [node]
  start = Node(node.val)
  cloned[node] = start
  
  while queue:
    current = queue.pop()
    for neighbor in current.neighbors:
      if neighbor not in cloned:
        clone_neighbor = Node(neighbor.val)
        cloned[neighbor] = clone_neighbor
        queue.append(neighbor)

      cloned[current].neighbors.append(cloned[neighbor])
  
  return start