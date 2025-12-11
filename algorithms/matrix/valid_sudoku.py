def isValidSudoku(board: list[list[str]]):
  for r in range(9):
    seen = set()
    for c in range(9):
      num = board[r][c]
      if num == ".":
        continue
      if num in seen:
        return False
      seen.add(num)
      
  for c in range(9):
    seen = set()
    for r in range(9):
      num = board[r][c]
      if num == ".":
        continue
      if num in seen:
        return False
      seen.add(num)
      
  for row_edge in range(0, 9, 3):
    for col_edge in range(0, 9, 3):
      seen = set()
      for r in range(row_edge, row_edge + 3):
        for c in range(col_edge, col_edge + 3):
          num = board[r][c]
          if num == ".":
            continue
          if num in seen:
            return False
          seen.add(num)

  return True

board_test_1 = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

board_test_2 = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

print(isValidSudoku(board_test_1))
print(isValidSudoku(board_test_2))