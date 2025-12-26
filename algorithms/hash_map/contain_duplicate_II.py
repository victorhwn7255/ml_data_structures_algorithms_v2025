def containsNearbyDuplicate(nums: list[int], k: int):
  table = {}
  
  for i in range(len(nums)):
    if nums[i] in table and i - table[nums[i]] <= k:
      return True
    else:
      table[nums[i]] = i
  
  return False

print(containsNearbyDuplicate([1,2,3,1], 3))
print(containsNearbyDuplicate([1,0,1,1], 1))
print(containsNearbyDuplicate([1,2,3,1,2,3], 2))