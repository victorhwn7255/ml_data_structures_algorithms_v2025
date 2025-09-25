def kidsWithCandies(candies:list[int], extraCandies: int) -> list[bool]:
  results = []
  largest = max(candies)
  
  for kid in candies:
    if kid + extraCandies >= largest:
      results.append(True)
    else:
      results.append(False)
  
  return results

candies_1 = [2,3,5,1,3]
extraCandies_1 = 3

print(kidsWithCandies(candies_1, extraCandies_1))