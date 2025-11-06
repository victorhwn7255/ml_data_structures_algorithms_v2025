def minCostClimbingStairs(cost: list[int]):
  n = len(cost)
  memo = [0] * n
  memo[0] = cost[0]
  memo[1] = cost[1]
  
  for i in range(2, n):
    memo[i] = cost[i] + min(memo[i-1], memo[i-2])
  
  return min(memo[-1], memo[-2])

cost_1 = [10,15,20]
cost_2 = [1,100,1,1,1,100,1,1,100,1]

print(minCostClimbingStairs(cost_1))
print(minCostClimbingStairs(cost_2))