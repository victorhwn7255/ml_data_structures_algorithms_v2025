def tribonacci(n):
  memo = [ 0, 1, 1 ]
  if n < 3:
    return memo[n]
  
  for i in range (3, n+1):
    memo.append(memo[i-1] + memo[i-2] + memo[i-3])
  
  return memo[n]

n_1 = 4
n_2 = 25

print(tribonacci(n_1))
print(tribonacci(n_2))