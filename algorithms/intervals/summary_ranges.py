def summaryRanges(nums: list[int]):
  i = 0
  result = []
  
  while i < len(nums):
    start = nums[i]
    j = i
    
    while j + 1 < len(nums) and nums[j + 1] == nums[j] + 1:
      j += 1
      
    if nums[j] == start:
      result.append(str(start))
    else:
      result.append(f"{start}->{nums[j]}")
  
    i = j + 1
    
  return result


print(summaryRanges([0,1,2,4,5,7]))
print(summaryRanges([0,2,3,4,6,8,9]))
