def uniquePaths(m, n):
  memo = [[0] * n for _ in range(m)]
  
  for i in range(0, m):
    memo[i][0] = 1
  for j in range(0, n):
    memo[0][j] = 1
    
  for i in range(1, m):
    for j in range(1, n):
      memo[i][j] = memo[i][j-1] + memo[i-1][j]
  
  return memo[m-1][n-1]

print(uniquePaths(3, 7))
print(uniquePaths(3, 2))