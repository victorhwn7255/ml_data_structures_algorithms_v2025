def threeSum(nums: list[int]):
  result = []
  nums.sort()
  
  for i in range(len(nums)):
    if nums[i] > 0:
      break
    if i > 0 and nums[i] == nums[i-1]:
      continue
    
    left = i+1
    right = len(nums)-1
    target = 0 - nums[i]
    
    while left < right:
      if nums[left] + nums[right] < target:
        left += 1
      elif nums[left] + nums[right] > target:
        right -= 1
      else:
        result.append([nums[i], nums[left], nums[right]])
        left += 1
        right -= 1
        while left < right and nums[left] == nums[left - 1]:
          left +=1
        while left < right and nums[right] == nums[right + 1]:
          right -=1
    
  return result

print(threeSum([-1,0,1,2,-1,-4]))
print(threeSum([0,1,1]))
print(threeSum([0,0,0]))