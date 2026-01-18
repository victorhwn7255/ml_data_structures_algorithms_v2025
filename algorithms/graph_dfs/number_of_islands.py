
def numIslands(grid: list[list[str]]):
  count = 0
  rows = len(grid)
  cols = len(grid[0])
  
  def sink(r, c):
    if r < 0 or r>= rows or c < 0 or c >= cols:
      return
    if grid[r][c] == '0':
      return
    
    grid[r][c] = '0'
    sink(r+1, c)
    sink(r, c+1)  
    sink(r-1, c)  
    sink(r, c-1)
    
  for r in range(rows):
    for c in range(cols):
      if grid[r][c] == '1':
        count += 1
        sink(r, c)  
  
  return count

test_grid_1 = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

test_grid_2 = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

print(numIslands(test_grid_1))
print(numIslands(test_grid_2))