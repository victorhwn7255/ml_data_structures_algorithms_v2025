def combine(n, k):
  result = []
  path = []
  def dfs(start, need):
    if need == 0:
      result.append(path.copy())
      return
      
    max_start = n - need + 1
    for i in range(start, max_start + 1):
      path.append(i)
      dfs(i+1, need-1)
      path.pop()
  
  dfs(1, k)
  return result

print(combine(4, 2))
print(combine(1, 1))