def generateParenthesis(n):
  results = []
  left_count = 1
  path = ['(']
  
  def backtrack(open_count, left_count, path:list):
    if len(path) == n*2:
      results.append(''.join(path))
      return
    
    if left_count > 0:
      path.append(')')
      backtrack(open_count, left_count-1, path)
      path.pop()
    
    if open_count < n:
      path.append('(')
      backtrack(open_count+1, left_count+1, path)
      path.pop()
  
  backtrack(1, left_count, path)
  return results

print(generateParenthesis(3))
print(generateParenthesis(1))