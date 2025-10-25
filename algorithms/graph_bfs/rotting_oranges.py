def orangesRotting(grid: list[list[int]]):
  directions = [(1, 0), (-1, 0), (0, 1), (0, -1)] # DOWN UP RIGHT LEFT
  queue = []
  m = len(grid) # ROW
  n = len(grid[0]) # COL
  fresh_count = 0
  max_time = 0
  
  for i in range(m):
    for j in range(n):
      if grid[i][j] == 2:
        queue.append((i, j, 0))
      elif grid[i][j] == 1:
        fresh_count += 1
        
  if fresh_count == 0:
    return 0
  
  while queue:
    row, col, time = queue.pop(0)
    
    for dr, dc in directions:
      new_row = row + dr
      new_col = col + dc
      
      if  0 <= new_row < m and 0 <= new_col < n and grid[new_row][new_col] == 1:
        grid[new_row][new_col] = 2
        fresh_count -= 1
        max_time = max(max_time, time + 1)
        queue.append((new_row, new_col, time + 1))
  
  return max_time if fresh_count == 0 else -1 


test_1 = [[2,1,1],[1,1,0],[0,1,1]]
test_2 = [[2,1,1],[0,1,1],[1,0,1]]
test_3 = [[0,2]]

print(orangesRotting(test_1))
print(orangesRotting(test_2))
print(orangesRotting(test_3))