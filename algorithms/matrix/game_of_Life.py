def gameOfLife(board: list[list[int]]):
  rows = len(board)
  cols = len(board[0])
  directions = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),           (0, 1),
    (1, -1), (1, 0),  (1, 1)
  ]
  
  for i in range(rows):
    for j in range(cols):
      count = 0
      for dr, dc in directions:
        nr, nc = i + dr, j + dc
        if 0 <= nr < rows and 0 <= nc < cols:
          if abs(board[nr][nc]) == 1:
            count += 1

      if board[i][j] == 1:
        if count < 2 or count > 3:
          board[i][j] = -1
      else:
        if count == 3:
          board[i][j] = 2
  
  for i in range(rows):
    for j in range(cols):
      if board[i][j] > 0:
        board[i][j] = 1
      else:
        board[i][j] = 0


test_board_1 = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
test_board_2 = [[1,1],[1,0]]

gameOfLife(test_board_1)
gameOfLife(test_board_2)

print(test_board_1)
print(test_board_2)