def maxProfit(prices: list[int], fee: int):
  hold = [0] * len(prices)
  cash = [0] * len(prices)
  hold[0] = -prices[0]
  cash[0] = 0
  
  for i in range(1, len(prices)):
    hold[i] = max(hold[i-1], cash[i-1] - prices[i])
    cash[i] = max(cash[i-1], hold[i-1] + prices[i] - fee)
  
  return cash[-1]


prices_1 = [1,3,2,8,4,9]
prices_2 = [1,3,7,5,10,3]

print(maxProfit(prices_1, 2))
print(maxProfit(prices_2, 3))