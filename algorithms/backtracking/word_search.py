def exist(board: list[list[str]], word: str):
  rows = len(board)
  cols = len(board[0])
  
  def backtrack(row, col, curr_string):
    if len(curr_string) == 0:
      return True
    
    target = curr_string[0]
    temp = board[row][col]
    board[row][col] = '#'
    directions =[[row+1, col], [row-1, col], [row, col+1], [row, col-1]]

    for dr, dc in directions:
      if 0 <= dr < rows and 0 <= dc < cols:
        if board[dr][dc] == target:
          if backtrack(dr, dc, curr_string[1:]):
            return True
    board[row][col] = temp
    return False
  
  for i in range(rows):
    for j in range(cols):
      if board[i][j] == word[0]:
        if backtrack(i, j, word[1:]):
          return True      

  return False


test_board = [
  ["A","B","C","E"],
  ["S","F","C","S"],
  ["A","D","E","E"]
]

print(exist(test_board, "ABCCED"))