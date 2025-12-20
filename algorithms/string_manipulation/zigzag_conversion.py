def convert(s: str, numRows: int):
  if numRows == 1 or numRows >= len(s):
    return s
  
  all_rows = [""] * numRows
  current_row = 0
  direction = 1
  
  for char in s:
    all_rows[current_row] += char
    
    if current_row == 0:
      direction = 1
    elif current_row == numRows - 1:
      direction = -1
      
    current_row += direction

  return "".join(all_rows)

print(convert("PAYPALISHIRING", 3))
print(convert("PAYPALISHIRING", 4))
print(convert("A", 1))