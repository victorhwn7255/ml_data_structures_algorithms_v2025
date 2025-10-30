import math

def successfulPairs(spells: list[int], potions: list[int], success: int):
  results = []
  potions.sort()
  
  for spell in spells:
    count = 0
    min_factor = math.ceil(success/spell)
    left = 0
    right = len(potions)
    
    while left < right:
      mid = (left + right) // 2
      if potions[mid] >= min_factor:
        right = mid
      else:
        left = mid + 1
    
    count = len(potions) - left
    results.append(count)
  
  return results


test_spells_1 = [5,1,3]
test_potions_1 = [1, 2, 3, 4, 5]
success_1 = 7

test_spells_2 = [3,1,2]
test_potions_2 = [8,5,8]
success_2 = 16

print(successfulPairs(test_spells_1, test_potions_1, success_1))
print(successfulPairs(test_spells_2, test_potions_2, success_2))