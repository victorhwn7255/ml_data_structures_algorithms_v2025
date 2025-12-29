def longestConsecutive(nums: list[int]):
  
  num_set = set(nums)
  result = 0
  
  for num in num_set:
    if num - 1 not in num_set:
      current = num
      length = 1
      
      while current + 1 in num_set:
        current += 1
        length += 1
        
      result = max(result, length)
  
  return result

print(longestConsecutive([0]))
print(longestConsecutive([100,4,200,1,3,2]))