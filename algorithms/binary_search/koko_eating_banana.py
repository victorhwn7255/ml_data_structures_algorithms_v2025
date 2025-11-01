from math import ceil

def minEatingSpeed(piles: list[int], h: int):
  left = 1
  right = max(piles)
  
  while left < right:
    mid = (left + right)//2
    total_hours = 0
    for pile in piles:
      hour_per_pile = ceil(pile/mid)
      total_hours += hour_per_pile
    if total_hours <= h:
      right = mid
    else:
      left = mid + 1
  
  return left


test_piles_1 = [3,6,7,11]
h_1 = 8
test_piles_2 = [30,11,23,4,20]
h_2 = 5
test_piles_3 = [30,11,23,4,20]
h_3 = 6

print(minEatingSpeed(test_piles_1, h_1))
print(minEatingSpeed(test_piles_2, h_2))
print(minEatingSpeed(test_piles_3, h_3))