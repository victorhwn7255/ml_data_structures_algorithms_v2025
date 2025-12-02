def maxProfit(prices: list[int]):
  max_profits = 0
  
  for i in range(1, len(prices)):
    if prices[i] > prices[i - 1]:
      max_profits += prices[i] - prices[i - 1]
  
  return max_profits

prices_1 = [7,1,5,3,6,4]
prices_2 = [1,2,3,4,5]
prices_3 = [7,6,4,3,1]

print(maxProfit(prices_1))
print(maxProfit(prices_2))
print(maxProfit(prices_3))