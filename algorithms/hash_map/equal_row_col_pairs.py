def equalPairs(grid: list[list[int]]) -> int:
  row_counts = {}
  num_rows = len(grid)
  num_cols = len(grid[0])
  count = 0
  
  for row in grid:
    row_tuple = tuple(row)
    if row_tuple not in row_counts:
      row_counts[row_tuple] = 0
    row_counts[row_tuple] += 1
    
  for j in range(num_cols):
    col = []
    for i in range(num_rows):
      col.append(grid[i][j])
    if tuple(col) in row_counts:
      count += row_counts[tuple(col)]
  
  return count



grid_1 = [[3,2,1],[1,7,6],[2,7,7]]
grid_2 = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]

print(equalPairs(grid_1))
print(equalPairs(grid_2))