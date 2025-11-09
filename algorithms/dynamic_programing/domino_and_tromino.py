def numTilings(n):
  if n == 1: 
    return 1
  if n == 2:
    return 2
  
  MOD = 10**9 + 7
  dp = [0] * (n+1)
  gap = [0] * (n+1)
  
  dp[1], dp[2] = 1, 2
  gap[1], gap[2] = 0, 1
  
  for i in range(3, n+1):
    dp[i] = (dp[i-1] + dp[i-2] + 2* gap[i-1]) % MOD
    gap[i] = (gap[i-1] + dp[i-2]) % MOD
  
  return dp[n]

print(numTilings(3))

