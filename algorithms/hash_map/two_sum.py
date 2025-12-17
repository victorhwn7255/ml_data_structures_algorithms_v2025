def twoSum(nums: list[int], target: int):
  table = {}
  
  for i in range(len(nums)):
    comp = target - nums[i]
    if comp in table:
      return [table[comp], i]
    else:
      table[nums[i]] = i


print(twoSum([2,7,11,15], 9))
print(twoSum([3,2,4], 6))
print(twoSum([3,3], 6))