def generateParenthesis(n: int):
  result = []
  
  def backtrack(path, open_used, closed_used):
    if len(path) == n * 2:
      result.append(path)
      
    if open_used < n:
      backtrack(path + "(", open_used + 1, closed_used)
    
    if closed_used < open_used:
      backtrack(path + ")", open_used, closed_used + 1)
      
  backtrack("", 0, 0)
  
  return result

print(generateParenthesis(3))