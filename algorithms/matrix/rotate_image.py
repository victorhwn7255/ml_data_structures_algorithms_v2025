def rotate(matrix: list[list[int]]):
  cols = len(matrix[0])
  rows = len(matrix)
  
  for i in range(rows):
    for j in range(i+1, cols):
      matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
      
  for i in range(rows):
    matrix[i].reverse()


matrix_1 = [[1,2,3],[4,5,6],[7,8,9]]
rotate(matrix_1)
print(matrix_1)