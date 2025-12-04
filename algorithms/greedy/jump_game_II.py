def jump(nums: list[int]):
  count = 0
  current_end = 0
  max_position = 0
  
  for i in range(len(nums) - 1):
    max_position = max(max_position, i + nums[i])
    
    if i == current_end:
      count += 1
      current_end = max_position
      
      if current_end >= len(nums) - 1:
        break
  
  return count



print(jump([2,3,1,1,4]))
print(jump([2,3,0,1,4]))