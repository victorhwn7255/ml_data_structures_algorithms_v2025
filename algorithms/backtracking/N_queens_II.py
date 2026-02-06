def totalNQueens(n: int):
  count = 0
  columns = set()
  diagnals = set()         # row - col
  anti_diagonals = set()   # row + col
  
  def backtrack(row):
    nonlocal count
    if row == n:
      count += 1
      return
    
    for col in range(n):
      if col in columns:
        continue
      if (row - col) in diagnals:
        continue
      if (row + col) in anti_diagonals:
        continue
      
      columns.add(col)
      diagnals.add(row - col)
      anti_diagonals.add(row + col)
      
      backtrack(row + 1)
      
      columns.remove(col)
      diagnals.remove(row - col)
      anti_diagonals.remove(row + col)
  
  backtrack(0)
  return count

print(totalNQueens(4))
print(totalNQueens(1))