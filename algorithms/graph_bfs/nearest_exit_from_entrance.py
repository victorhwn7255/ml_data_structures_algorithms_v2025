def nearestExit(maze: list[list[str]], entrance: list[int]):
  visited = set([(entrance[0], entrance[1])])
  queue = [(entrance[0], entrance[1], 0)]
  m = len(maze) # ROW num
  n = len(maze[0]) # COLUMN num
  
  directions = [(1, 0), (-1, 0), (0, 1), (0, -1)] # DOWN UP RIGHT LEFT
  
  while len(queue) > 0:
    r, c, steps = queue[0]
    queue = queue[1:]
  
    if(r in [0, m-1] or c in [0, n-1]) and [r, c] != entrance:
      return steps
    
    for dr, dc in directions:
      nr, nc = r + dr, c + dc
      if 0 <= nr < m and 0 <= nc < n and maze[nr][nc] == '.' and (nr, nc) not in visited:
        visited.add((nr, nc))
        queue.append((nr, nc, steps + 1))
  
  return -1




maze_1 = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]]
entrance_1 = [1, 2]

maze_2 = [["+","+","+"],[".",".","."],["+","+","+"]]
entrance_2 = [1, 0]

maze_3 = [[".","+"]]
entrance_3 = [0, 0]

print(nearestExit(maze_1, entrance_1))
print(nearestExit(maze_2, entrance_2))
print(nearestExit(maze_3, entrance_3))