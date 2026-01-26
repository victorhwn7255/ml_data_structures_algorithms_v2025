def snakesAndLadders(board: list[list[int]]):
  n = len(board)
  target = n * n
  
  queue = [(1, 0)]
  visited = set()
  visited.add(1)
  
  while queue:
    current_square, rolls = queue.pop(0)
    
    if current_square == target:
      return rolls
    
    for dice in range(1, 7):
      next_square = current_square + dice
      if next_square > target:
        continue
      idx = next_square - 1
      row_from_bottom = idx // n
      col_in_row = idx % n
      row = n - 1 - row_from_bottom
      if row_from_bottom % 2 == 0:
          col = col_in_row
      else:
          col = n - 1 - col_in_row
      if board[row][col] != -1:
        next_square = board[row][col]
      if next_square not in visited:
        visited.add(next_square)
        queue.append((next_square, rolls+1))
  
  return -1

test_board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]

print(snakesAndLadders(test_board))