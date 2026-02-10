def generateParenthesis(n):
  results = []
  left_count = 1
  path = ['(']
  
  def backtrack(left_count, path:list):
    if len(path) == n*2:
      results.append(''.join(path))
      return
    
    if left_count > 0:
      path.append(')')
      backtrack(left_count-1, path)
      path.pop()

    open_count = (len(path) + left_count) // 2
    
    if open_count < n:
      path.append('(')
      backtrack(left_count+1, path)
      path.pop()
  
  backtrack(left_count, path)
  return results

print(generateParenthesis(3))
print(generateParenthesis(1))