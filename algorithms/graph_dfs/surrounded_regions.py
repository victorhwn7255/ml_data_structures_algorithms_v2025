def solve(board: list[list[str]]):
  rows = len(board)
  cols = len(board[0])
  
  def dfs_mark_safe(r, c):
    if r < 0 or r >= rows or c < 0 or c >= cols:
      return
    if board[r][c] != 'O':
      return 
    board[r][c] = '#'
    dfs_mark_safe(r+1, c)
    dfs_mark_safe(r, c+1)
    dfs_mark_safe(r-1, c)
    dfs_mark_safe(r, c-1)
    
  for r in range(rows):
    if board[r][0] == 'O':
      dfs_mark_safe(r, 0)
    if board[r][cols-1] == 'O':
      dfs_mark_safe(r, cols-1)
  for c in range(cols):
    if board[0][c] == 'O':
      dfs_mark_safe(0, c)
    if board[rows-1][c] == 'O':
      dfs_mark_safe(rows-1, c)
      
  for r in range(rows):
    for c in range(cols):
      if board[r][c] == 'O':
        board[r][c] = 'X'
      elif board[r][c] == '#':
        board[r][c] = 'O'
  

test_board_1 = [
  ["X","X","X","X"],
  ["X","O","O","X"],
  ["X","X","O","X"],
  ["X","O","X","X"]
  ]

test_board_2 = [["X"]]

solve(test_board_1)
solve(test_board_2)

print(test_board_1)
print(test_board_2)