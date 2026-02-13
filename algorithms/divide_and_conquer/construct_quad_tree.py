class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
        
def construct(grid: list[list]):
  n = len(grid)
  
  def dfs(row, col, size):
    first_num = grid[row][col]
    all_same = True
    for r in range(row, row+size, 1):
      for c in range(col, col+size, 1):
        if grid[r][c] != first_num:
          all_same = False
          break
      if not all_same:
        break
        
    if all_same:
      return Node(first_num, True, None, None, None, None)
    
    half = size//2
    
    return Node(
      val = 0,
      isLeaf=False,
      topLeft= dfs(row, col, half),
      topRight=dfs(row, col+half, half),
      bottomLeft=dfs(row+half, col, half),
      bottomRight=dfs(row+half, col+half, half)
    )
  
  return dfs(0, 0, n)

test_grid = [
  [1,1,1,1,0,0,0,0],
  [1,1,1,1,0,0,0,0],
  [1,1,1,1,1,1,1,1],
  [1,1,1,1,1,1,1,1],
  [1,1,1,1,0,0,0,0],
  [1,1,1,1,0,0,0,0],
  [1,1,1,1,0,0,0,0],
  [1,1,1,1,0,0,0,0]
]

print(construct(test_grid))