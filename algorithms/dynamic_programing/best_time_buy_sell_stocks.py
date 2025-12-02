def maxProfit(prices: list[int]):
  max_profit = 0
  min_price = prices[0]
  
  for i in range(1, len(prices)):
    max_profit = max(max_profit, prices[i] - min_price)
    min_price = min(min_price, prices[i])
  
  return max_profit

prices_1 = [7,1,5,3,6,4]
prices_2 = [7,6,4,3,1]

print(maxProfit(prices_1))
print(maxProfit(prices_2))