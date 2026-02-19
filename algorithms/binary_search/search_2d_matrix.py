def searchMatrix(matrix: list[list[int]], target: int):
  rows = len(matrix)
  cols = len(matrix[0])
  
  if matrix[rows-1][0] < target:
    target_row = rows-1
  else:
    target_row = 0
  
  for row in range(rows):
    if matrix[row][0] == target:
      return True
    elif matrix[row][0] > target:
      target_row = row - 1
      break
  
  for col in range(cols):
    if matrix[target_row][col] == target:
      return True
    
  return False


print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))
print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13))
print(searchMatrix([[1],[3]], 1))
print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 30))