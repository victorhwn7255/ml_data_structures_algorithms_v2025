def setZeroes(matrix: list[list[int]]):
  rows = len(matrix)
  cols = len(matrix[0])
  zero_rows = set()
  zero_cols = set()
  
  for i in range(rows):
    for j in range(cols):
      if matrix[i][j] == 0:
        zero_rows.add(i)
        zero_cols.add(j)
  
  for row in zero_rows:
    for j in range(cols):
      matrix[row][j] = 0
  
  for col in zero_cols:
    for i in range(rows):
      matrix[i][col] = 0 

test_matrix_1 = [[1,1,1],[1,0,1],[1,1,1]]
test_matrix_2 = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]

setZeroes(test_matrix_1)
setZeroes(test_matrix_2)

print(test_matrix_1)
print(test_matrix_2)